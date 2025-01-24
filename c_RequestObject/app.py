from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Home route to render the form
@app.route('/')
def home():
    return render_template('signup.html')

# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve data from the form fields using the `request.form` object
    username = request.form.get('username')
    email = request.form.get('email')
    gender = request.form.get('gender')
    languages = request.form.getlist('languages')  # Retrieves list of checked boxes
    country = request.form.get('country')
    
    # Display the form data back to the user
    return f"""
    <h1>Form Data Submitted</h1>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Gender:</strong> {gender}</p>
    <p><strong>Programming Languages:</strong> {', '.join(languages)}</p>
    <p><strong>Country:</strong> {country}</p>
    """

# Route that handles query parameters
@app.route('/search')
def search():
    # Access query parameters using request.args
    search_query = request.args.get('query')  # Get the value of 'query' parameter
    category = request.args.get('category')  # Get the value of 'category' parameter

    # Respond with the query data
    return f"Search Results for: {search_query} in Category: {category}"

@app.route('/filter')
def filter_data():
    categories = request.args.getlist('category')  # Retrieves multiple categories
    return f"Filtering results for categories: {', '.join(categories)}"

# Route that handles JSON data
@app.route('/submitjson', methods=['POST'])
def submitjson():
    # Get JSON data from the request
    data = request.get_json()

    # Extract values from the JSON
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')

    # Respond with a message using the received data
    response = {
        "message": f"User {name} ({email}), age {age}, has been successfully submitted!"
    }

    return jsonify(response)
    

if __name__ == '__main__':
    app.run(debug=True)

