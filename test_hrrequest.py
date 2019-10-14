import unittest
import module.hrrequest as H
import time


class Testhrrequest(unittest.TestCase):

    def test_createHrRequest(self):
        hrr = H.HrRequest('role','desc', int(time.time()))
        self.assertTrue(hrr.createHrRequest('SMPM'))

        hrr2 = H.HrRequest('', '', int(time.time()))
        self.assertFalse(hrr2.createHrRequest('SMPM'))

    #
    def test_viewHrRequest(self):

        self.assertEqual(H.HrRequest.viewHrRequest('1570792395'),['role: role',
        'desc: desc',
        'hrrId: 1570792395',
        ''])

    def test_submit(self):
        self.assertTrue(H.HrRequest.submitTo('1570697825','HR'))
        self.assertFalse(H.HrRequest.submitTo('1570196546','HR'))




if __name__ == '__main__':
    unittest.main()