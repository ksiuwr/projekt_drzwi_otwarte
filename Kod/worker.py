from multiprocessing.connection import Listener
from repository import Repository
from door_lock import Door

WORKER_SOCKET_NAME = '/tmp/worker'
ADDER_SOCKET_NAME = '/tmp/adder'

username_to_add = None


def process_read_command(card_serial):
    # type: (str) -> None
    global username_to_add
    Repository.update_last_used(card_serial)

    if username_to_add:
        success = Repository.add_card(username_to_add, card_serial)
        if success:
            Repository.log_message(
                'add',
                card_serial + ' (' + username_to_add + ')')
        else:
            Repository.log_message(
                'error',
                'Failed to add card: ' + card_serial)

        username_to_add = None
        return

    if not Repository.is_authorized(card_serial):
        Repository.log_message('reject', '' + card_serial)
        return

    Repository.log_message(
        'open',
        card_serial + ' (' + Repository.get_name(card_serial) + ')')
    Door.open()


def process_add_command():
    # type: () -> None
    pass


def main():
    # type: () -> None
    listener = Listener(WORKER_SOCKET_NAME, 'AF_UNIX')
    try:
        Door.initialize()
        while True:
            conn = listener.accept()

            print('connection accepted from', listener.last_accepted)
            msg = conn.recv()
            print('Message: ', msg)
            command = msg['type']
            value = msg['value']

            if command == 'read':
                process_read_command(value)
            elif command == 'add':
                process_add_command()
            else:
                Repository.log_message('error', 'Unknown command: ' + command)

    finally:
        Door.cleanup()
        listener.close()


if __name__ == '__main__':
    main()
