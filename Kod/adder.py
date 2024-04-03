import re
import sys
import os
import pwd
from multiprocessing.connection import Listener
import messenger


def main() -> None:
    if pwd.getpwuid(os.getuid()).pw_name != 'pi':
        raise RuntimeError('Script must be run as "pi" user')

    listener = Listener('/tmp/adder', 'AF_UNIX')

    if len(sys.argv) == 1:
        print('Enter new users name')
        name = input('>')
    else:
        name = ' '.join(sys.argv[1:])

    while (re.match(r'\w+(?:\s\w+)+', name) is None or
           not all([w[0].isupper() for w in name.split()])):
        print(
            f"Wrong username pattern for {name}. "
            f"Expected format: 'Name Surname'\n")
        print('Enter new users name')
        name = input('>')

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
