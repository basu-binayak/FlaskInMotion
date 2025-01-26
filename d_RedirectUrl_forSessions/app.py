from flask import Flask, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# @app.route('/')
# def home():
#     return "Welcome to the homepage!"

# @app.route('/login')
# def login():
#     return "Please log in!"

@app.route('/guest')
def guest():
    return redirect(url_for('login'))  # Redirect to login page

@app.route('/profile/<username>')
def profile(username):
    return f"Profile page of {username}"

@app.route('/dashboard')
def dashboard():
    # Using url_for to generate the URL for 'profile' with a parameter
    return f"Go to {url_for('profile', username='Binayak')}"

@app.route('/details/<name>')
def details(name):
    location = request.args.get('location', 'India')
    return f"Hello, {name}! You're from {location}."

@app.route('/redirectDetails')
def redirectDetails():
    # redirect to the details route using url_for to generate the URL
    return redirect(url_for('details', name="Satya", location="Texas"))
    # http://127.0.0.1:5000/home/Satya?location=Texas

# Session in Flask
@app.route('/')
def home():
    if 'username' in session:
        username = session['username'] # or username = session.get('username')
        return f'Logged in as {username}'
    return 'You are not logged in!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') # Store username in session
        return redirect(url_for('home'))
    return '''
        <form method="post">
            <input type="text" name="username">
            <input type="submit" value="Log In">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)  # Clear session
    return redirect(url_for('home'))




if __name__ == '__main__':
    app.run(debug=True)

