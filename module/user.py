


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



