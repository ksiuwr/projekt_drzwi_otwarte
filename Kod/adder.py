from multiprocessing.connection import Listener
import sys
import messenger


def main() -> None:
    listener = Listener('/tmp/adder', 'AF_UNIX')

    if len(sys.argv) == 1:
        print('Enter new users name')
        name = input('>')
    else:
        name = ' '.join(sys.argv[1:])
    if messenger.send('/tmp/worker', {'type': 'add', 'value': name}):
        print('Now read a card with reader')

        conn = listener.accept()
        msg = conn.recv()

        if msg['type'] == 'ack':
            print('User added')
        else:
            print('Error: ' + msg['message'])

        conn.close()
    else:
        print("Couldn't establish connection with worker")

    listener.close()


if __name__ == "__main__":
    main()
