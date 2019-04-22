from flask import Flask, request, render_template


app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/register')
def index():
    return render_template('user-signup.html', username = '', password = '', passver = '', email = '', 
        username_error = '', password_error = '', passver_error = '', email_error='') 

@app.route('/register', methods = ['POST'])
def validate_info():

    username = request.form['username'] 

    password = request.form['password']

    passver = request.form['passver']

    email = request.form['email']

    username_error = ''
    password_error = ''
    passver_error = ''
    email_error = ''

    if not username:
        username_error = 'Username field must have a valid data type'
    else:
        if len(username) < 3 or len(username)> 20:
            username_error = "The Username must be 3-20 characters in lenght!"

    if not password:
        password_error = 'Password must not be empty'
    else:
        if password != passver:
            password_error = 'Your Password Must Match the Password in the Verification Field!'
            password = ''

    if not passver:
        passver_error = "Please enter the password again to verify"
    else:
        if passver != password:
           passver_error = 'Your Password Must Match the Password Field !'
           passver = ''

    if len(email)>0:
        if len(email)< 3 or len(email)>20:
            email_error = "Your email must be between 3-20 characters in lenght!"
        else:
            if '.' not in email:
                email_error = "Your email is missing a special character (@ or . )"
            elif '@' not in email: 
                email_error = "Your email is missing a special character (@ or . )"
            else:
                email_error=''

    if username_error or password_error or passver_error or email_error:
        return render_template('user-signup.html', username = username, password = password, passver = passver, email = email, 
        username_error = username_error, password_error = password_error, passver_error = passver_error, email_error=email_error)
    else:
        return render_template('welcome-page.html', username = username)

app.run()