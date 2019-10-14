import time
import module.event as E
import module.user as u
import module.task as T
import module.hrrequest as H
import module.budget as B
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def index():
    return render_template('login.html')


@app.route("/login")
def login():
    username = request.args.get("username")
    pw = request.args.get("password")
    # print(username,pw)

    if username == 'SCSO':
        [views, username, usr] = u.SCSO.login(username, pw)
        eventList =usr.getEventList()

        return render_template('event.html', user=username, views=views, eventList=eventList)
    elif username == 'FM':
        [views, username, usr] = u.FM.login(username, pw)
        eventList =usr.getEventList()
        budgetList =usr.getBudgetList()
        return render_template('event.html', user=username, views=views, eventList=eventList, budgetList=budgetList)
    elif username == 'AM':
        [views, username, usr] = u.FM.login(username, pw)
        eventList =usr.getEventList()
        return render_template('event.html', user=username, views=views, eventList=eventList)
    elif username == 'SMPM':
        [views, username, usr] = u.SMPM.login(username, pw)
        taskList =usr.getTaskList()
        HRList =usr.getHRList()
        budgetList =usr.getBudgetList()
        return render_template('event.html', user=username, views=views, taskList=taskList, HRList=HRList, budgetList=budgetList)
    elif username == 'subTeam1':
        [views, username, usr] = u.subTeam1.login(username, pw)
        taskList =usr.getTaskList()
        return render_template('event.html', user=username, views=views, taskList=taskList)
    elif username == 'subTeam2':
        [views, username, usr] = u.subTeam2.login(username, pw)
        taskList =usr.getTaskList()
        return render_template('event.html', user=username, views=views, taskList=taskList)
    elif username == 'HR':
        [views, username, usr] = u.subTeam2.login(username, pw)
        HRList = usr.getHRList()
        return render_template('event.html', user=username, views=views, HRList=HRList)
    elif username == 'CSO':
        [views, username, usr]=u.User.login(username,pw)

        # if user == 'SCSO':

        return render_template('event.html', user=username, views=views)
    else:
        return 'login failed'



@app.route("/createEvent")
def createEvent():
    clientName = request.args.get("clientName")
    eventName = request.args.get("eventName")
    startDate = request.args.get("startDate")
    endDate = request.args.get("endDate")
    budget = request.args.get("budget")
    submitTo = request.args.get("submitTo")


    newEvent = E.Event(clientName,eventName,startDate,endDate,budget,int(time.time()))
    if E.Event.createEvent(newEvent,submitTo):
        return '<a href="javascript:window.history.go(-1)"><- back</a><br> event created !'
    else:
        return '<a href="javascript:window.history.go(-1)"><- back</a><br> fail to create !'



@app.route("/viewEvent")
def viewEvent():

    eid = request.args.get("eventId")


    event = E.Event.viewEvent(eid)

    return {'event':event}


@app.route("/updateEvent")
def updateEvent():

    eid = request.args.get("eventId")
    who = request.args.get("user")
    t = request.args.get("type")

    res = E.Event.updateEvent(eid,who,t)

    if res == True:
        return {'res':t+' Successfully'}
    else :
        return {'res':t+' failed'}

    # return {'event':event}


@app.route("/submitEvent")
def submitEvent():

    to = request.args.get("to")
    eid = request.args.get("eventId")
    cmt = request.args.get("comment")
    F = request.args.get("from")
    print('cmt',cmt)

    res = E.Event.submitTo(eid,to, F,cmt)

    if res == True:
        return {'res':'submit Successfully'}
    else :
        return {'res':'submit failed'}

    # return {'event':event}

@app.route("/createTask")
def createTask():
    taskName = request.args.get("taskName")
    eventName = request.args.get("eventName")
    activity = request.args.get("activity")
    budget = request.args.get("budget")
    submitTo = request.args.get("submitTo")


    newTask = T.Task(taskName, eventName, activity, budget, int(time.time()))
    if T.Task.createTask(newTask,submitTo):
        return '<a href="javascript:window.history.go(-1)"><- back</a><br>task created !'
    else:
        return '<a href="javascript:window.history.go(-1)"><- back</a><br>fail to create !'

@app.route("/viewTask")
def viewTask():

    tid = request.args.get("taskId")


    task = T.Task.viewTask(tid)

    return {'task':task}


@app.route("/submitTask")
def submitTask():

    to = request.args.get("to")
    tid = request.args.get("taskId")
    cmt = request.args.get("comment")
    F = request.args.get("from")
    print('cmt',cmt)

    # if cmt !='':
    #     E.Event.submitTo(cmt, to)

    res = T.Task.submitTo(tid,to, F,cmt)

    if res == True:
        return {'res':'submit Successfully'}
    else :
        return {'res':'submit failed'}

    # return {'task':task}

@app.route("/createHrRequest")
def createHrRequest():
    role = request.args.get("role")
    desc = request.args.get("desc")
    submitTo = request.args.get("submitTo")


    newHrr = H.HrRequest(role, desc, int(time.time()))
    if H.HrRequest.createHrRequest(newHrr,submitTo):
        return '<a href="javascript:window.history.go(-1)"><- back</a><br>HR Request created !'
    else:
        return '<a href="javascript:window.history.go(-1)"><- back</a><br>fail to create !'

@app.route("/viewHiringRequest")
def viewHrRequest():

    hrrId = request.args.get("hrId")


    hrr = H.HrRequest.viewHrRequest(hrrId)

    return {'res':hrr}

@app.route("/updateHR")
def updateHR():

    to = request.args.get("to")
    hrrId = request.args.get("hrId")
    cmt = request.args.get("cmt")
    F = request.args.get("user")
    ty = request.args.get("type")
    print('cmt',cmt)

    res = H.HrRequest.submitTo(hrrId,to, ty, F, cmt)

    if res == True:
        return {'res':'submit Successfully'}
    else :
        return {'res':'submit failed'}

@app.route("/createBudgetRequest")
def createBudget():
    amount = request.args.get("amount")
    eventName = request.args.get("eventName")
    activity = request.args.get("activity")
    submitTo = request.args.get("submitTo")


    newBudget = B.Budget(amount, eventName, activity, int(time.time()))
    if B.Budget.createBudget(newBudget,submitTo):
        return '<a href="javascript:window.history.go(-1)"><- back</a><br> Budget Request created !'
    else:
        return '<a href="javascript:window.history.go(-1)"><- back</a><br> fail to create !'

@app.route("/viewBudgetRequest")
def viewBudget():

    budgetId = request.args.get("brId")


    budget = B.Budget.viewBudget(budgetId)

    return {'res':budget}


@app.route("/updateBudgetRequest")
def updateBudgetRequest():

    to = request.args.get("to")
    budgetId = request.args.get("brId")
    cmt = request.args.get("cmt")
    F = request.args.get("user")
    ty = request.args.get("type")
    print('cmt',cmt)

    res = B.Budget.submitTo(budgetId,to, ty, F, cmt)

    if res == True:
        return {'res':'submit Successfully'}
    else :
        return {'res':'submit failed'}

    # return {'event':event}

if __name__ == '__main__':
    app.run()
