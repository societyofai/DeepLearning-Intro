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

@app.route("/new_details", methods=['GET','POST'])
def new_details():
    if request.methods == 'POST':
        new_data = request.form
        username = new_data['username']
        classname = new_data['classname']
        new_data = {
            'username': username,
            'classname': classname
        }
        return render_template('new_details.html' , new_data = new_data)
    else:
        return render_template('new_details.html' , new_data = new_data)
if __name__ == "__main__":
    app.run()



