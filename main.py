from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") ## facebook.com -> feeds, messages notification, group notifications, status
def index():
    return "Hello World"

@app.route("/user")
def user_details():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()



