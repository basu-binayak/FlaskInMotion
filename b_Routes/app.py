from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the About page'

@app.route('/user', defaults={'name':'Binayak'})
@app.route('/user/<string:name>')
def user(name):
    return f'Hello {name}! Hope you journey of Flask is going great!'

# Route that handles GET and POST methods
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return "Form Submitted!"
    else:
        return "Submit Form"

# Route that handles PUT method
@app.route('/update', methods=['PUT'])
def update():
    return "Update Resource"

# Route that handles DELETE method
@app.route('/delete', methods=['DELETE'])
def delete():
    return "Delete Resource"

if __name__ == '__main__':
    app.run(debug=True)
