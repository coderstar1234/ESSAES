from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random secret key
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ESSAES'  # Change this to your MongoDB URI
mongo = PyMongo(app)
login_manager = LoginManager(app)

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id, username, email):
        self.id = user_id  # Unique identifier for the user
        self.username = username
        self.email = email

    def get_id(self):
        return str(self.id)  # Ensure the user_id is returned as a string

# Flask-Login loader function
@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'_id': user_id})
    if user_data:
        return User(user_data['_id'], user_data['username'], user_data['email'])
    return None

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/buzz')
def buzz():
    return render_template('buzz.html')

@app.route('/3DModel')
def model():
    return render_template('3DModel.html')

@app.route('/ResolveError')
def resolve_error():
    return render_template('ResolveError.html')

@app.route('/topic')
def topic():
    return render_template('topic.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_data = mongo.db.users.find_one({'email': email, 'password': password})
        if user_data:
            user = User(user_data['_id'], user_data['username'], user_data['email'])
            login_user(user)
            return redirect(url_for('home'))  # Redirect to the home page after successful sign-in
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_id = mongo.db.users.insert_one({'username': username, 'email': email, 'password': password}).inserted_id
        user = User(user_id, username, email)
        login_user(user)
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
