from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

WTF_CSRF_SECRET_KEY = "elephant"

app = Flask(__name__)
app.secret_key = "elephant"


class LoginForm(FlaskForm):
  # arguments given when creating StringField and PasswordField  is for the label property of the form field
  # prefer adding the keyword argument when it's not clear what the argument is for
  email = StringField(label="Email", validators=[DataRequired()])
  # represents <input type="text". Use for most of the more complicated fields.
  # Using PasswordField, it will obscure the text typed into the input
  password = PasswordField(label="Password", validators=[DataRequired()])
  # SubmitField, represents <input type="submit". This allows checking if submit button is pressed.
  submit = SubmitField(label="Log In")


@app.route("/login", methods=['POST', 'GET'])
def login():
  login_form = LoginForm()
  login_form.validate_on_submit()
  return render_template('login.html', form=login_form)


@app.route("/")
def home():
  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
