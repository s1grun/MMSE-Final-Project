from . import common

class Budget:
    def __init__(self, amount, eventName, activity, budgetId):
        self.amount = amount
        self.eventName = eventName
        self.activity = activity
        self.budgetId = budgetId

    def createBudget(self, to):

        if int(self.amount)<=0:
            return False
        else:
            fname = str(self.budgetId)

            f = open('./storage/budget/'+fname, 'w')
            f.write('amount: '+ self.amount + '\n')
            f.write('eventName: '+ self.eventName + '\n')
            f.write('activity: '+ self.activity + '\n')
            f.write('budgetId: '+ str(self.budgetId) + '\n')
            f.close()

            self.submitTo(fname, to)
            f = open('./storage/SMPM_budget', 'a')
            f.write(str(self.budgetId) + ' unread\n')
            f.close()

        return True

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
    def submitTo(budgetId, to, ty=None, From=None, cmt=None):

        if to == 'SMPM':
            to = 'SMPM_budget'
        elif to == 'FM':
            to = 'FM_budget'

        common.updateFile(to, budgetId, budgetId + ' unread\n')

        if cmt is not None and cmt != '':
            f2 = open('./storage/budget/' + budgetId, 'a')
            f2.write('comment ' + cmt + '\n')
            f2.close()

        if ty is not None:
            f2 = open('./storage/budget/' + budgetId, 'a')
            f2.write(ty + 'ed by ' + From + '\n')
            f2.close()


        if From is not None:
            From = From + '_budget'
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


