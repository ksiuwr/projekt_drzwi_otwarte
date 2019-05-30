from multiprocessing.connection import Client
from os.path import exists


def send(socket, message):
    # (string, object) -> bool
    if not exists(socket):
        return False
    connection = Client(socket, 'AF_UNIX')
    connection.send(message)
    connection.close()
    return True
