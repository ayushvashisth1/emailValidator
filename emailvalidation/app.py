# app.py
from flask import Flask, render_template, request

# Create a Flask web application instance and specify the template folder
# as the current directory. This allows index.html to be in the same
# directory as app.py.
app = Flask(__name__, template_folder='.')

# Define the email validation logic in a function.
def validate_email(email):
    """
    Validates an email string based on specific criteria.
    
    Args:
        email (str): The email string to validate.

    Returns:
        str: A validation message indicating if the email is valid or why it is invalid.
    """
    # Rule 1: Minimum length of 6 characters.
    if len(email) < 6:
        return "Invalid email: should be at least 6 characters long."
    
    # Rule 2: Should not start with '@' or '.'
    if email[0] == '@' or email[0] == '.':
        return "Invalid email: should not start with '@' or '.'"
        
    # Rule 3: Must contain exactly one '@' and one '.'
    # Note: The original logic for a single '.' is very restrictive.
    # We will implement it exactly as you provided.
    if email.count('@') != 1 or email.count('.') != 1:
        return "Invalid email: should contain exactly one '@' and one '.'"

    # Rule 4: Check position of '.'
    # The original logic uses a bitwise XOR (^) to check if the dot is either
    # the 3rd or 4th character from the end, but not both.
    # This is a very specific rule and might fail for many valid emails.
    if not ((email[-4] == '.') ^ (email[-3] == '.')):
        return "Invalid email: '.' should be at least 2 characters after '@' (based on the original logic)."
        
    # Rule 5: Should not contain spaces.
    if ' ' in email:
        return "Invalid email: should not contain spaces."

    # If all checks pass, the email is valid.
    return "Valid email!"

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handles the main page request.
    
    If it's a POST request, it validates the email and passes the result
    to the template. Otherwise, it just renders the form.
    """
    result_message = None
    if request.method == 'POST':
        email_address = request.form.get('email')
        result_message = validate_email(email_address)

    return render_template('index.html', result=result_message)

if __name__ == '__main__':
    # Run the application in debug mode.
    # The debug=True option automatically reloads the server on code changes.
    app.run(debug=True)
