class Base:
    def __init__(self):
        # Lock the door on system startup.
        self.lock()

    def unlock(self):
        self.unlocked = True
        self.stateChanged()

    def lock(self):
        self.unlocked = False
        self.stateChanged()

    def stateChanged(self):
        pass

    def isUnlocked(self):
        return self.unlocked

    def needsCleanup(self):
        return False

    def stop(self):
        pass


class Debug(Base):
    def stateChanged(self):
        print("doors unlocked = %s" % self.unlocked)


try:
    import RPi.GPIO as GPIO

    class RPi(Base):
        LOCK_PIN = 18

        def __init__(self):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(RPi.LOCK_PIN, GPIO.OUT)
            super().__init__()

        def stateChanged(self):
            if self.unlocked:
                GPIO.output(RPi.LOCK_PIN, GPIO.LOW)
            else:
                GPIO.output(RPi.LOCK_PIN, GPIO.HIGH)

        def needsCleanup(self):
            return True

        def stop(self):
            GPIO.cleanup()

    class Auto(RPi):
        pass

except ImportError:
    # Not running on RPi, so DoorIO.RPi is unavailable
    class Auto(Debug):
        pass
