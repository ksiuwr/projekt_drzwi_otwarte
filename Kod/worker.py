from multiprocessing.connection import Listener

ADDER_PORT = 4003
WORKER_PORT = 4004
HOST = 'localhost'

address = (HOST, WORKER_PORT)
listener = Listener(address)

while True:
    conn = listener.accept()

    print 'connection accepted from', listener.last_accepted
    msg = conn.recv()
    print(msg)

    listener.close()

# from multiprocessing.connection import Client

# address = ('localhost', 6000)
# conn = Client(address, authkey='secret password')
# conn.send('close')
# # can also send arbitrary objects:
# # conn.send(['a', 2.5, None, int, sum])
# conn.close()