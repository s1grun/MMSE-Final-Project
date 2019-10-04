







class Event:
    def __init__(self, clientName, eventName, startDate, endDate, budget, eventId):
        self.clientName = clientName
        self.eventName = eventName
        self.startDate = startDate
        self.endDate = endDate
        self.budget = budget
        self.eventId = eventId

    def createEvent(self, submitTo):

        fname = str(self.eventId)

        if checkDate(self.startDate,self.endDate):

            f = open('../storage/event/'+fname,'w')
            f.write('clientName:'+ self.clientName)
            f.write('eventName:'+ self.eventName)
            f.write('startDate:'+ self.startDate)
            f.write('endDate:'+ self.endDate)
            f.write('budget:'+ str(self.budget))
            f.write('eventId:'+ str(self.eventId))
            f.close()
            return True
        else:
            return False




    def viewEvent(self, eventId):

        fname = str(eventId)
        f = open('../storage/event/' + fname, 'r')
        event = f.read()
        f.close()

        return event




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
