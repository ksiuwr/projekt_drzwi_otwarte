import unittest
import time
import DoorController
from DoorState import DoorState


class TestDoorState(unittest.TestCase):
    def test_unlock_once(self):
        state = DoorState(DoorController.Base)
        state.start()
        state.unlock()
        time.sleep(0.05)
        self.assertEqual(state.isUnlocked(), True)
        state.stop()

    def test_lock(self):
        state = DoorState(DoorController.Base, unlockTime=0.1)
        state.start()
        state.unlock()
        time.sleep(0.2)
        self.assertEqual(state.isUnlocked(), False)
        state.stop()

    def test_multiple(self):
        state = DoorState(DoorController.Base, unlockTime=0.3)
        state.start()
        state.unlock()
        time.sleep(0.2)
        state.unlock()
        time.sleep(0.2)
        self.assertEqual(state.isUnlocked(), True)
        time.sleep(0.3)
        self.assertEqual(state.isUnlocked(), False)
        state.stop()
