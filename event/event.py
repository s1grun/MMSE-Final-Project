







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
        f = open('../storage/event/'+fname,'w')
        f.write('clientName:'+ self.clientName)
        f.write('eventName:'+ self.eventName)
        f.write('startDate:'+ self.startDate)
        f.write('endDate:'+ self.endDate)
        f.write('budget:'+ str(self.budget))
        f.write('eventId:'+ str(self.eventId))
        f.close()

        return True


    def viewEvent(self, eventId):

        fname = str(eventId)
        f = open('../storage/event/' + fname, 'r')
        event = f.read()
        f.close()

        return event


