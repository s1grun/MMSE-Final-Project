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

        self.assertEqual(E.Event.viewEvent('1570196545'),['clientName: A',
 'eventName: test',
 'startDate: 2019-10-23',
 'endDate: 2019-10-24',
 'budget: 5',
 'eventId: 1570533529',
 'reject by SCSO',
 ''])

    def test_submit(self):
        self.assertTrue(E.Event.submitTo('1570196545','SCSO'))
        self.assertFalse(E.Event.submitTo('1570196546','SCSO'))




if __name__ == '__main__':
    unittest.main()