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
        return render_template('index.html', user=username, views=views, eventList=eventList)

    [views, username, usr]=u.User.login(username,pw)

    # if user == 'SCSO':

    return render_template('index.html', user=username, views=views)




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


@app.route("/rejectEvent")
def viewEvent():

    eid = request.args.get("eventId")


    event = E.Event.rejectEvent(eid)

    return {'event':event}



if __name__ == '__main__':
    app.run()
