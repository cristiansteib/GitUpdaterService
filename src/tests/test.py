import unittest
from modules import updater


class TestUpdater(unittest.TestCase):

    def setUp(self):
        updater.Updater()


if __name__ == '__main__':
    unittest.main()