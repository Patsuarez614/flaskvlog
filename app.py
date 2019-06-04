from flask import Flask, render_template, url_for
from forms import Registration, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = ''61543402761b43e623f8fbac6783b14f''

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')    

@app.route("/register")
def register():
	form = RegistrationForm()
    return render_template('register.html', title='Register', form=sorm)      