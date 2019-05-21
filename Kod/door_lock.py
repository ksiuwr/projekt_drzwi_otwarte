from time import sleep
import RPi.GPIO as GPIO  # pylint: disable=import-error

DOOR_LOCK_PIN = 18


def open_door():
    # type: () -> None
    GPIO.output(DOOR_LOCK_PIN, GPIO.LOW)
    sleep(2)
    GPIO.output(DOOR_LOCK_PIN, GPIO.HIGH)


def initialize_door():
    # type: () -> None
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DOOR_LOCK_PIN, GPIO.OUT)
    GPIO.output(DOOR_LOCK_PIN, GPIO.HIGH)


def cleanup_door():
    # type: () -> None
    GPIO.cleanup()
