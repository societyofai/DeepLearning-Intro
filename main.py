from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") ## facebook.com -> feeds, messages notification, group notifications, status
def index():
    return "Hello World"

@app.route("/user")
def user_details():
    return render_template('index.html')

@app.route("/details", methods=['GET', 'POST'])
def details():
    if request.method == 'POST': ## post method
        data = request.form
        username = data['username']
        # print("username given to the user was", username)
        # return "POST method was called"
        # return "username given to the user was {}".format(username)
        data = {
            'username': username
        }
        return render_template('details.html', data = data)
    else: ## get method
        return render_template('details.html')

if __name__ == "__main__":
    app.run()



