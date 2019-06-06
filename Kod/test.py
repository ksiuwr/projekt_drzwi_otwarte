from time import sleep

from py532lib.i2c import Pn532_i2c
import RPi.GPIO as GPIO

from repository import Repository

START_OF_SERIAL = 14
SERIAL_LENGTH = 8
DOOR_LOCK_PIN = 18


def prety(to_prety):
    # type: (str) -> str
    res = []
    for idx in range(0, len(to_prety), 2):
        res.append(to_prety[idx:idx+2])
    return " ".join(res)


def get_serial(byte_array):
    # type: (bytearray) -> str
    hex_data = bytes(byte_array).hex()
    return hex_data[START_OF_SERIAL:START_OF_SERIAL+SERIAL_LENGTH]


def open_door():
    # type: () -> None
    GPIO.output(DOOR_LOCK_PIN, GPIO.LOW)
    sleep(2)
    GPIO.output(DOOR_LOCK_PIN, GPIO.HIGH)


def initializeGPIO():
    # type: () -> None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DOOR_LOCK_PIN, GPIO.OUT)
    GPIO.output(DOOR_LOCK_PIN, GPIO.HIGH)


def main():
    # type: () -> None
    pn532 = Pn532_i2c()
    pn532.SAMconfigure()
    initializeGPIO()
    try:
        while True:
            card_data = pn532.read_mifare().get_data()
            serial_number = get_serial(card_data)
            if Repository.is_authorized(serial_number):
                Repository.update_last_used(serial_number)
                open_door()
    except KeyboardInterrupt:
        GPIO.cleanup()

def test_card():
    # type: () -> None
    pn532 = Pn532_i2c()
    pn532.SAMconfigure() 
    while True:
        card_data = pn532.read_mifare().get_data()
        serial_number = get_serial(card_data)
        pretty = prety(str(bytes(card_data), 'utf-8'))
        print('Serial number:', serial_number)
        print('All data     :', pretty)
        sleep(2)


if __name__ == "__main__":
    main()
