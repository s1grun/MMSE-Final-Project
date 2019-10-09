class hrrequest:
    def __init__(self, role, desc, hrrId):
        self.role = role
        self. desc = desc
        self.budgetId = budgetId

    def createhrRequest(self, to):
        fname = str(self.hrrId)

        f = open('./storage/hrr/'+fname, 'w')
        f.write('role: '+ self.role + '\n')
        f.write('desc: '+ self.desc + '\n')
        f.write('hrrId: '+ str(self.hrrId) + '\n')
        f.close()

        #self.submitTo(fname, to)