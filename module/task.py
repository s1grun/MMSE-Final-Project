from . import common
import os.path

class Task:
    def __init__(self, taskName, eventName, activity, budget, taskId):
        self.taskName = taskName
        self.eventName = eventName
        self.activity = activity
        self.budget = int(budget)
        self.taskId = taskId

    def createTask(self, to):
        fname = str(self.taskId)

        f = open('./storage/task/'+fname, 'w')

        if self.budget > 0:
            f.write('taskName: '+ self.taskName + '\n')
            f.write('eventName: '+ self.eventName + '\n')
            f.write('activity: '+ self.activity + '\n')
            f.write('budget: '+ str(self.budget) + '\n')
            f.write('taskId: '+ str(self.taskId) + '\n')
            f.close()

            self.submitTo(fname, to)

            f = open('./storage/SMPM_task', 'a')
            f.write(str(self.taskId) + ' unread\n')
            f.close()

            return True
        else:
            return False


    @staticmethod
    def viewTask(taskId):

        if os.path.isfile('./storage/task/' + str(taskId)):
            fname = str(taskId)
            f = open('./storage/task/' + fname, 'r')
            task = f.read()
            # print(task)
            f.close()
            taskArr = task.split('\n')

            return taskArr
        else:
            return ['task not found']



    @staticmethod
    def submitTo(taskId, to, From=None, cmt=None):

        if os.path.isfile('./storage/task/' + taskId):
            if to == 'SMPM':
                to = 'SMPM_task'

            common.updateFile(to, taskId, taskId + ' unread\n')


            if cmt is not None and cmt!='':
                f2 = open('./storage/task/' + taskId, 'a')
                f2.write('comment ' + cmt + '\n')
                f2.close()

            if From is not None:
                f = open('./storage/' + From, 'r+')
                lines = f.read()
                lines = lines.split('\n')
                # print(lines)
                new_line_arr = []
                for line in lines:
                    print(str(line.split(' ')[0]))
                    if line.split(' ')[0] == taskId:
                        new_line_arr.append(taskId + ' read\n')
                    else:
                        new_line_arr.append(line + '\n')
                f.close()

                f = open('./storage/' + From, 'w')

                newStr = ''.join(new_line_arr)
                f.write(newStr)
                # print(task)
                f.close()

            return True
        else:
            return False
