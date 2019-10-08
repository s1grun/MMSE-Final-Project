







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

            self.submitTo(fname,to)
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
    @staticmethod
    def submitTo(eventId, to, From=None, cmt=None):

        f = open('./storage/' + to, 'a')
        f.write(eventId+' unread\n')
        f.close()

        if cmt is not None and cmt!='':
            f2 = open('./storage/event/' + eventId, 'a')
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
                if line.split(' ')[0] == eventId:
                    new_line_arr.append(eventId + ' read\n')
                else:
                    new_line_arr.append(line + '\n')
            f.close()

            f = open('./storage/' + From, 'w')

            newStr = ''.join(new_line_arr)
            f.write(newStr)
            # print(event)
            f.close()

        return True

    @staticmethod
    def updateEvent(eventId, who, t):

        # fname = str(eventId)
        f = open('./storage/' + who, 'r+')
        lines = f.read()
        lines = lines.split('\n')
        print(lines)
        new_line_arr = []
        for line in lines:
            print(str(line.split(' ')[0]))
            if line.split(' ')[0] == eventId:
                new_line_arr.append(eventId+' read\n')
            else:
                new_line_arr.append(line+'\n')
        f.close()

        f = open('./storage/' + who, 'w')

        newStr = ''.join(new_line_arr)
        f.write(newStr)
        # print(event)
        f.close()

        f2 = open('./storage/event/' + eventId, 'a')
        f2.write(t+'ed by '+who+'\n')
        f2.close()


        return True




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
