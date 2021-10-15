from time import sleep
import RPi.GPIO as GPIO


class Buzzer:
    BUZZ_PIN = 21

    @staticmethod
    def buzz(buzz_time: float = 2, buzz_amount: int = 1) -> None:
        for i in range(buzz_amount):
            GPIO.output(Buzzer.BUZZ_PIN, GPIO.HIGH)
            sleep(buzz_time)
            GPIO.output(Buzzer.BUZZ_PIN, GPIO.LOW)
            sleep(buzz_time/2)

    @staticmethod
    def initialize() -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Buzzer.BUZZ_PIN, GPIO.OUT)

    @staticmethod
    def cleanup() -> None:
        GPIO.cleanup()
