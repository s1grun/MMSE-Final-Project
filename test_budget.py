import unittest
import module.budget as B
import time


class TestBudget(unittest.TestCase):

    def test_createBudget(self):
        self.id1= int(time.time())
        b1 = B.Budget('100','t1', 'activity', self.id1)
        self.assertTrue(b1.createBudget('FM'))

        self.id2 = self.id1+1
        b2 = B.Budget('-1', 't2', 'activity', self.id2)
        self.assertFalse(b2.createBudget('FM'))

    #
    def test_viewTask(self):

        self.assertEqual(B.Budget.viewBudget(self.id1),'taskName: Test Task eventName: Test Event activity:Food budget:34 taskId:1570619530')





if __name__ == '__main__':
    unittest.main()
