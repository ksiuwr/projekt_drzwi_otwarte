from threading import Thread, Event
import time
import DoorController


class DoorState(Thread):
    """This thread will manage the door lock state"""
    def __init__(self, controller=DoorController.Auto, unlockTime=8.0):
        self.doorController = controller()
        self.waitForChild = self.doorController.needsCleanup()
        super().__init__(
            name="GlobalLock",
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
                self.doorController.unlock()
                while self.unlockEvent.isSet():
                    # unless another event comes in,
                    # this loop will only execute once
                    self.unlockEvent.clear()
                    time.sleep(self.unlockTime)
                self.doorController.lock()

    def unlock(self):
        self.unlockEvent.set()

    def stop(self):
        self.running = False

    def isUnlocked(self):
        return self.doorController.isUnlocked()
