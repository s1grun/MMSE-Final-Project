


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
            print(usr)
        elif username == 'CSO':
            usr = CSO(username, password)
        elif username == 'FM':
            usr = FM(username, password)

        elif username == 'AM':
            usr = AM(username, password)

        elif username == 'SMPM':
            usr = SMPM(username, password)

        elif username == 'subTeam':
            usr = subTeam(username, password)


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
        self.viewList = ['createTask', 'viewTask', 'createHiringRequest']
        return self.viewList
    def getTaskList(self):

        fname = str('SMPM')
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr

class subTeam(User):

    def getViewList(self):
        self.viewList = ['viewTask']
        return self.viewList
    def getTaskList(self):

        fname = str('subTeam')
        f = open('./storage/' + fname, 'r')
        taskList = f.read()
        f.close()
        taskArr = taskList.split('\n')

        return taskArr