import unittest
import time
import DoorIO
from DoorManager import DoorManager


class TestDoorManager(unittest.TestCase):
    def test_unlock_once(self):
        state = DoorManager(DoorIO.Base)
        state.start()
        state.unlock()
        time.sleep(0.2)
        self.assertEqual(state.isUnlocked(), True)
        state.stop()

    def test_lock(self):
        state = DoorManager(DoorIO.Base, unlockTime=0.1)
        state.start()
        state.unlock()
        time.sleep(0.3)
        self.assertEqual(state.isUnlocked(), False)
        state.stop()

    def test_multiple(self):
        state = DoorManager(DoorIO.Base, unlockTime=0.3)
        state.start()
        state.unlock()
        time.sleep(0.2)
        state.unlock()
        time.sleep(0.2)
        self.assertEqual(state.isUnlocked(), True)
        time.sleep(0.3)
        self.assertEqual(state.isUnlocked(), False)
        state.stop()
