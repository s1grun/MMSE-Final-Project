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
    def test_viewBudget(self):

        self.assertEqual(B.Budget.viewBudget(1570791541),['amount: 345345','eventName: Test Event','activity: Food','budgetId: 1570791541','rejected by FM',''])


    def test_submit(self):
        self.assertTrue(B.Budget.submitTo('1570714776','HR'))
        self.assertFalse(B.Budget.submitTo('1570196546','HR'))



if __name__ == '__main__':
    unittest.main()
