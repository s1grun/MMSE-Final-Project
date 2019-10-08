from flask import Flask,request,render_template

import module.user as u
import module.event as E
import time
app = Flask(__name__, static_url_path='/static')


# @app.route('/')
# def hello_world():
#     # name = request.args.get("name", "World")
#     return 'Hello World!'

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
        return render_template('event.html', user=username, views=views, eventList=eventList)
    elif username == 'AM':
        [views, username, usr] = u.FM.login(username, pw)
        eventList =usr.getEventList()
        return render_template('event.html', user=username, views=views, eventList=eventList)

    [views, username, usr]=u.User.login(username,pw)

    # if user == 'SCSO':

    return render_template('event.html', user=username, views=views)




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
        return 'event created !'
    else:
        return 'fail to create !'



@app.route("/viewEvent")
def viewEvent():

    eid = request.args.get("eventId")


    event = E.Event.viewEvent(eid)

    return {'event':event}
    # if E.Event.createEvent(newEvent,submitTo):
    #     return 'event created !'
    # else:
    #     return 'fail to create !'


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

    # if cmt !='':
    #     E.Event.submitTo(cmt, to)

    res = E.Event.submitTo(eid,to, F,cmt)

    if res == True:
        return {'res':'submit Successfully'}
    else :
        return {'res':'submit failed'}

    # return {'event':event}


if __name__ == '__main__':
    app.run()
