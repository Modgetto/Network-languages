from flask import Flask, render_template, session, redirect, url_for, request, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample users data
users = {
    'admin': {'password': 'adminpass', 'role': 'admin'},
    'moderator': {'password': 'modpass', 'role': 'moderator'},
    'user': {'password': 'userpass', 'role': 'user'}
}

# Decorator for role-based access control
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'logged_in' not in session:
                return redirect(url_for('login'))
            if session.get('role') != role:
                return redirect(url_for('unauthorized'))
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and user['password'] == password:
            session['logged_in'] = True
            session['username'] = username
            session['role'] = user['role']
            return redirect(url_for('welcome'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/welcome')
def welcome():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', role=session.get('role'))

@app.route('/admin')
@role_required('admin')
def admin():
    return 'Admin Page: Full Access'

@app.route('/moderator')
@role_required('moderator')
def moderator():
    return 'Moderator Page: Edit Records and Comments'

@app.route('/user')
@role_required('user')
def user():
    return 'User Page: Create Records and View Friend Feed'

@app.route('/unauthorized')
def unauthorized():
    return 'Unauthorized Access', 403

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        if username in users:
            flash('Username already exists')
        else:
            users[username] = {'password': password, 'role': role}
            flash('User created successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/assign_role', methods=['GET', 'POST'])
@role_required('admin')
def assign_role():
    if request.method == 'POST':
        username = request.form['username']
        new_role = request.form['role']
        if username not in users:
            flash('User does not exist')
        else:
            users[username]['role'] = new_role
            flash('Role updated successfully')
    return render_template('assign_role.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
