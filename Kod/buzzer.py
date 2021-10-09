from time import sleep
import RPi.GPIO as GPIO


class Buzzer:
    BUZZ_PIN = 21

    @staticmethod
    def buzz(buzz_time: int = 2) -> None:
        GPIO.output(Buzzer.BUZZ_PIN, GPIO.HIGH)
        sleep(buzz_time)
        GPIO.output(Buzzer.BUZZ_PIN, GPIO.LOW)

    @staticmethod
    def initialize() -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Buzzer.BUZZ_PIN, GPIO.OUT)

    @staticmethod
    def cleanup() -> None:
        GPIO.cleanup()
