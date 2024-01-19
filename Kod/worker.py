from multiprocessing.connection import Listener
from repository import Repository
from door_lock import Door
from buzzer import Buzzer
import messenger

from typing import Optional

WORKER_SOCKET_NAME = '/tmp/worker'
ADDER_SOCKET_NAME = '/tmp/adder'

ACK = 'ack'
ERROR = 'error'


def respond_adder(success: bool, username: str, card_serial: str) -> None:
    message = {
        'type': ACK if success else ERROR,
        'message': '{} ({})'.format(card_serial, username)
    }

    messenger.send(ADDER_SOCKET_NAME, message)


def process_read_command(
        card_serial: str, username_to_add: Optional[str]) -> None:
    Repository.update_last_used(card_serial)

    if username_to_add:
        success = Repository.add_card(username_to_add, card_serial)
        respond_adder(success, username_to_add, card_serial)
        if success:
            Repository.log_message(
                'add',
                '{} ({})'.format(card_serial, username_to_add))
            Buzzer.buzz(3)
        else:
            Repository.log_message(
                'error',
                'Failed to add card: {}'.format(card_serial))

        return

    if not Repository.is_authorized(card_serial):
        Repository.log_message('reject', str(card_serial))
        Buzzer.buzz(0.5, 3)
        return

    Repository.log_message(
        'open',
        '{} ({})'.format(card_serial, Repository.get_name(card_serial)))
    Buzzer.buzz(0.1)
    Door.open()
    return


def process_add_command(value: str) -> str:
    return value


def process_open_command(value: str) -> None:
    try:
        opening_time = int(value)
    except ValueError:
        Repository.log_message(
            'error',
            'Failed to open the door. {} is not an integer.'.format(value))

    if 1 < opening_time <= 60:
        Door.open(opening_time)
    else:
        Repository.log_message(
            'error',
            'Failed to open the door. Opening time should be from 2 to 60. '
            'Got {} instead'.format(value))


def main() -> None:
    listener = Listener(WORKER_SOCKET_NAME, 'AF_UNIX')
    try:
        Door.initialize()
        Buzzer.initialize()
        name_to_add = None
        print('Worker started')
        while True:
            conn = listener.accept()

            print('connection accepted from', listener.last_accepted)
            msg = conn.recv()
            print('Message: ', msg)
            command = msg['type']
            value = msg['value']

            if command == 'read':
                process_read_command(value, name_to_add)
                name_to_add = None
            elif command == 'add':
                name_to_add = process_add_command(value)
            elif command == 'open':
                process_open_command(value)
            else:
                Repository.log_message(
                    'error',
                    'Unknown command: {}'.format(command))

    finally:
        Door.cleanup()
        Buzzer.cleanup()
        listener.close()


if __name__ == '__main__':
    main()
