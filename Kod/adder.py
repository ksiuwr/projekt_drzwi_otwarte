from multiprocessing.connection import Listener
import messenger


def main():
    listener = Listener('/tmp/adder', 'AF_UNIX')

    print('Enter new users name')
    name = input('>')
    if messenger.send('/tmp/worker', {'type': 'add', 'value': name}):
        print('Now read a card with reader')

        conn = listener.accept()
        msg = conn.recv()

        if msg['type'] == 'ack':
            print('User added')
        else:
            print('Error: ' + msg['value'])
    else:
        print("Couldn't establish connection with worker")

    conn.close()
    listener.close()


if __name__ == "__main__":
    main()
