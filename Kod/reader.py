from time import sleep
from py532lib.i2c import Pn532_i2c

import messenger

START_OF_SERIAL = 14
SERIAL_LENGTH = 8
READ_INTERVAL = 7


def get_serial(byte_array: bytearray) -> str:
    hex_data = bytes(byte_array).hex()
    return hex_data[START_OF_SERIAL:START_OF_SERIAL+SERIAL_LENGTH]


def main() -> None:
    pn532 = Pn532_i2c()
    pn532.SAMconfigure()

    print('Reader started')
    while True:
        card_data = pn532.read_mifare().get_data()
        serial_number = get_serial(card_data)
        messenger.send('/tmp/worker', {'type': 'read', 'value': serial_number})
        sleep(READ_INTERVAL)


if __name__ == "__main__":
    main()
