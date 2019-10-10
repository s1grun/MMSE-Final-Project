


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def login(username, password):
        usr =''
        print(username)
        if username == 'SCSO':
            usr = SCSO(username, password)
            # print(usr)
        elif username == 'CSO':
            usr = CSO(username, password)
        elif username == 'FM':
            usr = FM(username, password)

        elif username == 'AM':
            usr = AM(username, password)

        elif username == 'SMPM':
            usr = SMPM(username, password)

        elif username == 'subTeam1':
            usr = subTeam1(username, password)

        elif username == 'subTeam2':
            usr = subTeam2(username, password)

        elif username == 'HR':
            usr = HR(username, password)


        return [usr.getViewList(), username, usr]
        # return usr





class SCSO(User):

    def getViewList(self):
        self.viewList = ['viewEvent']
        return self.viewList

    def getEventList(self):

        fname = str('SCSO')
        f = open('./storage/' + fname, 'r')
        eventList = f.read()
        f.close()
        eventArr = eventList.split('\n')

        return eventArr



class CSO(User):

    def getViewList(self):
        self.viewList = ['createEvent']
        return self.viewList



class FM(User):

    def getViewList(self):
        self.viewList = ['viewEvent']
        return self.viewList
    def getEventList(self):

        fname = str('FM')
        f = open('./storage/' + fname, 'r')
        eventList = f.read()
        f.close()
        eventArr = eventList.split('\n')

        return eventArr


class AM(User):

    def getViewList(self):
        self.viewList = ['viewEvent']
        return self.viewList
    def getEventList(self):

        fname = str('AM')
        f = open('./storage/' + fname, 'r')
        eventList = f.read()
        f.close()
        eventArr = eventList.split('\n')

        return eventArr

class SMPM(User):

    def getViewList(self):
        self.viewList = ['createTask', 'viewTask', 'createHiringRequest', 'createBudgetRequest']
        return self.viewList
    def getTaskList(self):

        fname = 'SMPM_task'
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr

    def getHRList(self):
        fname = 'SMPM_hr'
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr
    def getBudgetList(self):
        fname = 'SMPM_budget'
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr

class subTeam1(User):

    def getViewList(self):
        self.viewList = ['viewTask']
        return self.viewList
    def getTaskList(self):

        fname = str('subTeam1')
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        # print(taskList)
        taskArr = taskList.split('\n')

        return taskArr

class subTeam2(User):

    def getViewList(self):
        self.viewList = ['viewTask']
        return self.viewList
    def getTaskList(self):

        fname = str('subTeam2')
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr




class HR(User):

    def getViewList(self):
        self.viewList = ['viewHrr']
        return self.viewList
    def getHRList(self):

        fname = str('HR')
        f = open('./storage/' + fname, 'r')
        hrrList = f.read()
        f.close()
        hrrArr = hrrList.split('\n')

        return hrrArr