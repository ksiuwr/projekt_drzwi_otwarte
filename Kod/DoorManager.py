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
        self.lastUnlockRequestTime = None
        self.unlockTime = unlockTime

    def run(self):
        """Don't run this directly, use start() instead"""
        while self.running:
            if self.lastUnlockRequestTime is not None:
                if time.time() - self.lastUnlockRequestTime > self.unlockTime:
                    self.io.lock()
                else:
                    self.io.unlock()
            time.sleep(0.1)

    def unlock(self):
        self.lastUnlockRequestTime = time.time()

    def stop(self):
        self.running = False

    def isUnlocked(self):
        return self.io.isUnlocked()
