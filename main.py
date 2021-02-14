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
        
        data = {
            'username': username
        }
        return render_template('details.html', data = data)
    else: ## get method
        return render_template('details.html')



@app.route("/detail_of_user", methods=['GET', 'POST'])
def detail_of_user():
    if request.method == 'POST': 
        data = request.form
        username = data['username']
        class_user=data['class_user']        
        data = {
            'username': username,
            'class': class_user
        }
        return render_template('list_output.html', data = data)
    else: ## get method
        return render_template('list_output.html')



if __name__ == "__main__":
    app.run()



