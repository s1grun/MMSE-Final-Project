import unittest
import module.task as T
import time


class TestTask(unittest.TestCase):

    def test_createTask(self):
        task = T.Task('taskName','t1', 'activity', 100, int(time.time()))
        self.assertTrue(task.creatTask('subTeam'))

        task2 = T.Task('taskName', 't2', 'activity', 100, int(time.time()))
        self.assertFalse(task2.createTask('subTeam'))

    #
    def test_viewTask(self):

        self.assertEqual(T.Task.viewTask('1570619530'),'taskName: Test Task eventName: Test Event activity:Food budget:34 taskId:1570619530')





if __name__ == '__main__':
    unittest.main()