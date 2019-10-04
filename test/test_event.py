import unittest
import module.event as E
import time


class TestEvent(unittest.TestCase):

    def test_createEvent(self):
        event = E.Event('clientname','e1', '2019-01-10', '2019-01-11', 100, int(time.time()))
        self.assertTrue(event.createEvent('SCSO'))

        event2 = E.Event('clientname', 'e2', '2019-01-11', '2019-01-10', 100, int(time.time()))
        self.assertFalse(event2.createEvent('SCSO'))

    #
    def test_viewEvent(self):

        self.assertEqual(E.Event.viewEvent('1570178326.103391'),'clientName:clientnameeventName:e1startDate:2019-01-10endDate:2019-01-11budget:100eventId:1570178326.103391')





if __name__ == '__main__':
    unittest.main()