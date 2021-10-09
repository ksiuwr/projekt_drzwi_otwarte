from multiprocessing.connection import Client
from os.path import exists
from typing import Any, Dict


def send(socket: str, message: Dict[str, Any]) -> bool:
    if not exists(socket):
        return False
    connection = Client(socket, 'AF_UNIX')
    connection.send(message)
    connection.close()
    return True
