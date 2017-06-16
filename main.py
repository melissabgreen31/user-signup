from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG']=True



@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route('/validate_info', methods= ['POST'])
def find_errors():
    template = jinja_env.get_template('form.html')
    username = request.form['username']
    password = request.form['password']
    confirmation = request.form['confirmation']
    email = request.form['email']

    username_error = ''
    password_error = ''
    confirmation_error = ''
    email_error = ''

    if len(username) > 20 or len(username) <3: 
        username_error = "That's not a valid username"
        usename = ''
        
    
    if len(password) > 20 or len(password) < 3:
        password_error = "That's not a valid password"
        

    if not confirmation == password or len(confirmation) >20 or len(confirmation) < 3:
        confirmation_error = "Passwords do not match"

    if '@' and '.' not in email:
       email_error = "Invalid Email"
       email = ''
        

    if not username_error and not password_error and not confirmation_error and not email_error:
        username = request.form['username']
        return redirect('/welcome?username={0}'.format(username))
    else:
        return template.render(username_error = username_error, password_error = password_error, confirmation_error = confirmation_error, email_error = email_error, username= username, email= email)

    

@app.route('/welcome')
def welcome():
    template = jinja_env.get_template('welcome.html')
    return template.render()

    
   


app.run()