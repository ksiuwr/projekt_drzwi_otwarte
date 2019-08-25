import sys
import messenger


def main():
    # () -> None
    opening_time = sys.argv if len(sys.argv) > 1 else "5"
    messenger.send('/tmp/worker', {'type': 'read', 'value': opening_time})


if __name__ == '__main__':
    main()
