from multiprocessing.connection import Listener
from typing import Optional
from repository import Repository
from door_lock import Door
import messenger


WORKER_SOCKET_NAME = '/tmp/worker'
ADDER_SOCKET_NAME = '/tmp/adder'

ACK = 'ack'
ERROR = 'error'


def respond_adder(success, username, card_serial):
    # type (bool, str, str) -> None
    message = {
        'type': ACK if success else ERROR,
        'message': '{} ({})'.format(card_serial, username)
    }

    messenger.send(ADDER_SOCKET_NAME, message)


def process_read_command(card_serial, username_to_add):
    # type: (str, Optional[str]) -> None
    Repository.update_last_used(card_serial)

    if username_to_add:
        success = Repository.add_card(username_to_add, card_serial)
        respond_adder(success, username_to_add, card_serial)
        if success:
            Repository.log_message(
                'add',
                '{} ({})'.format(card_serial, username_to_add))
        else:
            Repository.log_message(
                'error',
                'Failed to add card: {}'.format(card_serial))

        return None

    if not Repository.is_authorized(card_serial):
        Repository.log_message('reject', str(card_serial))
        return None

    Repository.log_message(
        'open',
        '{} ({})'.format(card_serial, Repository.get_name(card_serial)))
    Door.open()


def process_add_command(value):
    # type: (str) -> str
    return value


def main():
    # type: () -> None
    listener = Listener(WORKER_SOCKET_NAME, 'AF_UNIX')
    try:
        Door.initialize()
        name_to_add = None
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
            else:
                Repository.log_message(
                    'error',
                    'Unknown command: {}'.format(command))

    finally:
        Door.cleanup()
        listener.close()


if __name__ == '__main__':
    main()
