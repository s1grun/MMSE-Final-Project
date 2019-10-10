from . import common

class HrRequest:
    def __init__(self, role, desc, hrrId):
        self.role = role
        self. desc = desc
        self.hrrId = hrrId

    def createHrRequest(self, to):
        fname = str(self.hrrId)

        f = open('./storage/hrr/'+fname, 'w')
        f.write('role: '+ self.role + '\n')
        f.write('desc: '+ self.desc + '\n')
        f.write('hrrId: '+ str(self.hrrId) + '\n')
        f.close()

        self.submitTo(fname, to)
        f = open('./storage/SMPM_hr', 'a')
        f.write(str(self.hrrId) + ' unread\n')
        f.close()
        return True

    @staticmethod
    def viewHrRequest(hrrId):

        fname = str(hrrId)
        f = open('./storage/hrr/' + fname, 'r')
        hrrequest = f.read()
        # print(event)
        f.close()
        hrrequestArr = hrrequest.split('\n')

        return hrrequestArr

    @staticmethod
    def submitTo(hrrId, to, ty=None, From=None, cmt=None):

        if to == 'SMPM':
            to = 'SMPM_hr'

        # f = open('./storage/' + to, 'a')
        # f.write(hrrId + ' unread\n')
        # f.close()
        common.updateFile(to, hrrId, hrrId + ' unread\n')

        if cmt is not None and cmt != '':
            f2 = open('./storage/hrr/' + hrrId, 'a')
            f2.write('comment ' + cmt + '\n')
            f2.close()
        if ty is not None:
            f2 = open('./storage/hrr/' + hrrId, 'a')
            f2.write(ty + 'ed by ' + From + '\n')
            f2.close()

        if From is not None:
            f = open('./storage/' + From, 'r+')
            lines = f.read()
            lines = lines.split('\n')
            # print(lines)
            new_line_arr = []
            for line in lines:
                print(str(line.split(' ')[0]))
                if line.split(' ')[0] == hrrId:
                    new_line_arr.append(hrrId + ' read\n')
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
    def updateHrRequest(hrrId, who, t):

        # fname = str(eventId)
        f = open('./storage/' + who, 'r+')
        lines = f.read()
        lines = lines.split('\n')
        print(lines)
        new_line_arr = []
        for line in lines:
            print(str(line.split(' ')[0]))
            if line.split(' ')[0] == hrrId:
                new_line_arr.append(hrrId + ' read\n')
            else:
                new_line_arr.append(line + '\n')
        f.close()

        f = open('./storage/' + who, 'w')

        newStr = ''.join(new_line_arr)
        f.write(newStr)
        # print(event)
        f.close()

        f2 = open('./storage/event/' + hrrId, 'a')
        f2.write(t + 'ed by ' + who + '\n')
        f2.close()

        return True