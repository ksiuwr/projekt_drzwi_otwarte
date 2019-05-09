from multiprocessing.connection import Listener, Client


def main():
    listener = Listener(('localhost', 4003))
    address = ('localhost', 4004)
    outConn = Client(address)

    print('Enter new users name')
    name = input('>')
    outConn.send({'type': 'add', 'value': name})
    print('Now read a card with reader')

    conn = listener.accept()
    msg = conn.recv()
    if msg['type'] == 'ack':
        print('User added')
    else:
        print('Error: ' + msg['value'])
    conn.close()
    listener.close()


if __name__ == "__main__":
    main()
