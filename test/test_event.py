import unittest
import event.event as E
import time


class TestEvent(unittest.TestCase):

    def test_createEvent(self):
        event = E.Event('clientname','e1', '2019-01-10', '2019-01-11', 100, time.time())
        self.assertTrue(event.createEvent('scso'))

        event2 = E.Event('clientname', 'e2', '2019-01-11', '2019-01-10', 100, time.time())
        self.assertFalse(event2.createEvent('scso'))

    #
    # def test_viewEvent(self):
    #     self.assertEqual(E.viewEvent('1'))





if __name__ == '__main__':
    unittest.main()