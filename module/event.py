







class Event:
    def __init__(self, clientName, eventName, startDate, endDate, budget, eventId):
        self.clientName = clientName
        self.eventName = eventName
        self.startDate = startDate
        self.endDate = endDate
        self.budget = budget
        self.eventId = eventId

    def createEvent(self, to):

        fname = str(self.eventId)

        if checkDate(self.startDate,self.endDate):

            f = open('./storage/event/'+fname,'w')
            f.write('clientName: '+ self.clientName + '\n')
            f.write('eventName: '+ self.eventName+ '\n')
            f.write('startDate: '+ self.startDate+ '\n')
            f.write('endDate: '+ self.endDate+ '\n')
            f.write('budget: '+ str(self.budget)+ '\n')
            f.write('eventId: '+ str(self.eventId)+ '\n')
            f.close()

            self.submitTo(to)
            return True
        else:
            return False

    @staticmethod
    def viewEvent(eventId):

        fname = str(eventId)
        f = open('./storage/event/' + fname, 'r')
        event = f.read()
        # print(event)
        f.close()
        eventArr = event.split('\n')

        return eventArr

    def submitTo(self, to):

        f = open('./storage/' + to, 'a')
        f.write(str(self.eventId)+' unread\n')
        f.close()




def checkDate(start, end):


    year_s, mon_s, day_s = start.split('-')
    year_e, mon_e, day_e = end.split('-')
    year_s = int(year_s)
    mon_s = int(mon_s)
    day_s = int(day_s)
    year_e = int(year_e)
    mon_e = int(mon_e)
    day_e = int(day_e)
    if year_e < year_s:
        return False
    elif year_s == year_e and mon_e < mon_s:
        return False
    elif year_s == year_e and mon_e == mon_s and day_e < day_s:
        return False
    else:
        return True
