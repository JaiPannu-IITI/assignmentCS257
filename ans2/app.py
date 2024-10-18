from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route to display the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route to handle form submission
@app.route('/register', methods=['POST'])
def register():
    user_id = request.form['userId']
    password = request.form['password']
    
    # Simple validation
    if len(user_id) < 5:
        return render_template('login.html', message="User ID must be at least 5 characters long.")
    elif len(password) < 6:
        return render_template('login.html', message="Password must be at least 6 characters long.")
    else:
        # Here you can handle registration logic, like storing the user credentials
        return render_template('login.html', message="Registration successful!")

if __name__ == '__main__':
    app.run(debug=True)
