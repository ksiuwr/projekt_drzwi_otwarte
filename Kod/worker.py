from multiprocessing.connection import Listener
from repository import (
    add_card,
    get_name,
    is_authorized,
    log_message,
    update_last_used
)
from door_lock import cleanup_door, initialize_door, open_door

WORKER_SOCKET_NAME = '/tmp/worker'
ADDER_SOCKET_NAME = '/tmp/adder'

username_to_add = None


def process_read_command(card_serial):
    # type: (str) -> None
    global username_to_add
    update_last_used(card_serial)

    if username_to_add:
        success = add_card(username_to_add, card_serial)
        if success:
            log_message('add', '' + card_serial + ' (' + username_to_add + ')')
        else:
            log_message('error', 'Failed to add card: ' + card_serial)

        username_to_add = None
        return

    if not is_authorized(card_serial):
        log_message('reject', '' + card_serial)
        return

    log_message('open', '' + card_serial + ' (' + get_name(card_serial) + ')')
    open_door()


def process_add_command():
    # type: () -> None
    pass


def main():
    # type: () -> None
    listener = Listener(WORKER_SOCKET_NAME, 'AF_UNIX')
    try:
        initialize_door()
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
                log_message('error', 'Unknown command: ' + command)

    finally:
        cleanup_door()
        listener.close()


if __name__ == '__main__':
    main()
