 ```
# Import the necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    # Render the home page template
    return render_template('home.html')

# Define the route to register a party attendee
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the request method is GET, render the registration form
    if request.method == 'GET':
        return render_template('register.html')
    # If the request method is POST, process the form data
    else:
        # Get the form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Add the attendee to the database
        # ...

        # Redirect to the home page
        return redirect(url_for('home'))

# Define the route to view the list of party attendees
@app.route('/attendees')
def attendees():
    # Get the list of attendees from the database
    # ...

    # Render the attendees page template
    return render_template('attendees.html', attendees=attendees)

# Run the application
if __name__ == '__main__':
    app.run()
```