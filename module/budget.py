class Budget:
    def __init__(self, amount, eventName, activity, budgetId):
        self.amount = amount
        self.eventName = eventName
        self.activity = activity
        self.budgetId = budgetId

    def createBudget(self, to):
        fname = str(self.budgetId)

        f = open('./storage/budget/'+fname, 'w')
        f.write('amount: '+ self.amount + '\n')
        f.write('eventName: '+ self.eventName + '\n')
        f.write('activity: '+ self.activity + '\n')
        f.write('budgetId: '+ str(self.budgetId) + '\n')
        f.close()

        self.submitTo(fname, to)
        self.submitTo(fname, 'SMPM')

    @staticmethod
    def viewBudget(budgetId):

        fname = str(budgetId)
        f = open('./storage/budget/' + fname, 'r')
        budget = f.read()
        # print(budget)
        f.close()
        budgetArr = budget.split('\n')

        return budgetArr

    @staticmethod
    def submitTo(budgetId, to, From=None, cmt=None):

        f = open('./storage/' + to, 'a')
        f.write(budgetId + ' unread\n')
        f.close()

        if cmt is not None and cmt != '':
            f2 = open('./storage/budget/' + budgetId, 'a')
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
                if line.split(' ')[0] == budgetId:
                    new_line_arr.append(budgetId + ' read\n')
                else:
                    new_line_arr.append(line + '\n')
            f.close()

            f = open('./storage/' + From, 'w')

            newStr = ''.join(new_line_arr)
            f.write(newStr)
            # print(budget)
            f.close()

        return True

    @staticmethod
    def updateBudget(budgetId, who, t):

        # fname = str(budgetId)
        f = open('./storage/' + who, 'r+')
        lines = f.read()
        lines = lines.split('\n')
        print(lines)
        new_line_arr = []
        for line in lines:
            print(str(line.split(' ')[0]))
            if line.split(' ')[0] == budgetId:
                new_line_arr.append(budgetId + ' ' + t + '\n')
            else:
                new_line_arr.append(line + '\n')
        f.close()

        f = open('./storage/' + who, 'w')

        newStr = ''.join(new_line_arr)
        f.write(newStr)
        # print(budget)
        f.close()

        f2 = open('./storage/budget/' + budgetId, 'a')
        f2.write(t + 'ed by ' + who + '\n')
        f2.close()

        return True


