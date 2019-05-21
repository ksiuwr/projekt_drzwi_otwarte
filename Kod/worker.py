from multiprocessing.connection import Listener

listener = Listener('/tmp/worker', 'AF_UNIX')

while True:
    conn = listener.accept()

    print('connection accepted from', listener.last_accepted)
    msg = conn.recv()
    command = msg['type']
    if command == 'read':
        pass
    elif command == 'add':
        pass
    
    print(msg)

    listener.close()

# from multiprocessing.connection import Client

# address = ('localhost', 6000)
# conn = Client(address, authkey='secret password')
# conn.send('close')
# # can also send arbitrary objects:
# # conn.send(['a', 2.5, None, int, sum])
# conn.close()
