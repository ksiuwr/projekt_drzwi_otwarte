import sys
from time import sleep

import messenger


def main():
    # () -> None
    opening_time = sys.argv[1] if len(sys.argv) > 1 else "5"
    print("Try to open the door for {} seconds.".format(opening_time))
    messenger.send('/tmp/worker', {'type': 'open', 'value': opening_time})
    sleep(int(opening_time))
    print("Door closed")


if __name__ == '__main__':
    main()
