import sys
import messenger


def main():
    # () -> None
    opening_time = sys.argv[1] if len(sys.argv) > 1 else "5"
    messenger.send('/tmp/worker', {'type': 'open', 'value': opening_time})


if __name__ == '__main__':
    main()
