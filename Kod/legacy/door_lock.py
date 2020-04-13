from time import sleep
import RPi.GPIO as GPIO


class Door:
    LOCK_PIN = 18
    OPEN_INTERVAL = 2

    @staticmethod
    def open(opening_time=OPEN_INTERVAL):
        # type: (int) -> None
        GPIO.output(Door.LOCK_PIN, GPIO.LOW)
        sleep(opening_time)
        GPIO.output(Door.LOCK_PIN, GPIO.HIGH)

    @staticmethod
    def initialize():
        # type: () -> None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Door.LOCK_PIN, GPIO.OUT)
        GPIO.output(Door.LOCK_PIN, GPIO.HIGH)

    @staticmethod
    def cleanup():
        # type: () -> None
        GPIO.cleanup()
