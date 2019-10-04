from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    # name = request.args.get("name", "World")
    return 'Hello World!'

@app.route("/test")
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()
