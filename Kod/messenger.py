from multiprocessing.connection import Client
from os.path import isfile


def send(socket, message):
    # (string, object) -> bool
    if not isfile(socket):
        return False
    connection = Client(socket, 'AF_UNIX')
    connection.send(message)
    connection.close()
    return True
