from threading import Thread, Event
import time
import DoorIO


class DoorManager(Thread):
    """This thread will manage the door lock state"""
    def __init__(self, io=DoorIO.Auto, unlockTime=8.0):
        self.io = io()
        self.waitForChild = self.io.needsCleanup()
        name = "%s for %s.%s" % (
            type(self).__name__,
            io.__module__, io.__name__
        )
        super().__init__(
            name=name,
            target=self,
            daemon=not self.waitForChild
        )
        self.running = True
        self.unlockEvent = Event()
        self.unlockTime = unlockTime

    def run(self):
        """Don't run this directly, use start() instead"""
        while self.running:
            gotEvent = self.unlockEvent.wait(timeout=0.1)
            if gotEvent:
                self.io.unlock()
                while self.unlockEvent.isSet():
                    # unless another event comes in,
                    # this loop will only execute once
                    self.unlockEvent.clear()
                    time.sleep(self.unlockTime)
                self.io.lock()

    def unlock(self):
        self.unlockEvent.set()

    def stop(self):
        self.running = False

    def isUnlocked(self):
        return self.io.isUnlocked()
