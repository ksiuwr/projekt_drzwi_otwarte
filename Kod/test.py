from py532lib.i2c import Pn532_i2c
# from py532lib.frame import *
# from py532lib.constants import *

START_OF_SERIAL = 14
SERIAL_LENGTH = 8


def prety(to_prety: str) -> str:
    res = []
    for idx in range(0, len(to_prety), 2):
        res.append(to_prety[idx:idx+2])
    return " ".join(res)


def get_serial(byte_array: bytearray) -> str:
    hex_data = bytes(byte_array).hex()
    return hex_data[START_OF_SERIAL:START_OF_SERIAL+SERIAL_LENGTH]


def main() -> None:
    pn532 = Pn532_i2c()
    pn532.SAMconfigure()

    while(True):
        card_data = pn532.read_mifare().get_data()
        print(card_data)
        print(get_serial(card_data))
        # print(prety(bytes(card_data).hex()))

        # print([x for x in card_data])


if __name__ == "__main__":
    main()
