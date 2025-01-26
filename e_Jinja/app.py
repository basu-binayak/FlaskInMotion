from flask import Flask, render_template, request, redirect, url_for, session
import filters

app = Flask(__name__)

# Register the custom filter with the Jinja environment
app.jinja_env.filters['reverse'] = filters.reverse_filter
app.jinja_env.filters['isLessThan100'] = filters.comment_lessThan_100

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    user = session.get('username', 'Guest')
    languages = session.get('programmingList')
    comment = session.get('comments')
    return render_template('home.html', user=user, languages=languages, 
                           comment =comment)
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        session['programmingList'] = request.form.getlist('languages')
        session['comments'] = request.form.get('comment')
        return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/profile')
def profile():
    if 'username' in session:
        username = session['username']
        return render_template('profile.html', username=username)
    return redirect(url_for('login'))

@app.route('/settings')
def settings():
    if 'username' in session:
        user = session.get('username', 'Guest')
        languages = session.get('programmingList')
        comment = session.get('comments')
        return render_template('settings.html', username=user, languages = languages,
                               comment = comment)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
