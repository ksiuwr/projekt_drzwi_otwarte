from multiprocessing.connection import Client
from time import sleep
from py532lib.i2c import Pn532_i2c


START_OF_SERIAL = 14
SERIAL_LENGTH = 8
READ_INTERVAL = 3

def get_serial(byte_array):
    # type: (bytearray) -> str
    hex_data = bytes(byte_array).hex()
    return hex_data[START_OF_SERIAL:START_OF_SERIAL+SERIAL_LENGTH]


def main():
    # type: () -> None
    pn532 = Pn532_i2c()
    pn532.SAMconfigure()

    while True:
        card_data = pn532.read_mifare().get_data()
        serial_number = get_serial(card_data)
        connection = Client('/tmp/worker', 'AF_UNIX')
        connection.send({'type': 'read', 'value': serial_number})
        connection.close()
        sleep(READ_INTERVAL)


if __name__ == "__main__":
    main()
