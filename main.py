from flask import Flask

app = Flask(__name__)

@app.route("/") ## facebook.com -> feeds, messages notification, group notifications, status
def index():
    return "Hello World"

@app.route("/hi") ## facebook.com/messages.
def hi_route():
    return "Hi user"

if __name__ == "__main__":
    app.run()



