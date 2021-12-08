from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

WTF_CSRF_SECRET_KEY = "elephant"

app = Flask(__name__)
app.secret_key = "elephant"


class LoginForm(FlaskForm):
  # arguments given when creating StringField and PasswordField  is for the label property of the form field
  # prefer adding the keyword argument when it's not clear what the argument is for
  email = StringField(label="Email", validators=[DataRequired(), Email()])
  # represents <input type="text". Use for most of the more complicated fields.
  # Using PasswordField, it will obscure the text typed into the input
  password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
  # SubmitField, represents <input type="submit". This allows checking if submit button is pressed.
  submit = SubmitField(label="Log In")


@app.route("/login", methods=['POST', 'GET'])
def login():
  login_form = LoginForm()
  # Check validate_on_submit is True
  if login_form.validate_on_submit():
    # Gather data from user's input
    user_email = login_form.email.data
    user_password = int(login_form.password.data)
    # Check if the user's email/password match the credentials
    if user_email == "admin@email.com" and user_password == 12345678:
      # If it matches, show success page.
      return render_template('success.html')
    else:
      # If it doesn't match, show fail page.
      return render_template('denied.html')
  return render_template('login.html', form=login_form)


@app.route("/")
def home():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
