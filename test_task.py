import unittest
import module.task as T
import time


class TestTask(unittest.TestCase):

    def test_createTask(self):
        task = T.Task('taskName','t1', 'activity', 100, int(time.time()))
        self.assertTrue(task.createTask('SMPM'))

        task2 = T.Task('taskName', 't2', 'activity', -100, int(time.time()))
        self.assertFalse(task2.createTask('SMPM'))

    #
    def test_viewTask(self):

        self.assertEqual(T.Task.viewTask('1570619530'),['taskName: Test Task',
        'eventName: Test Event',
        'activity: Food',
        'budget: 342',
        'taskId: 1570619530',
        ''])


    def test_submit(self):
        self.assertTrue(T.Task.submitTo('1570719547','subTeam1'))
        self.assertFalse(T.Task.submitTo('1570196546','subTeam1'))


if __name__ == '__main__':
    unittest.main()