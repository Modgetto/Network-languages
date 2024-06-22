from flask import Flask, render_template

app = Flask(__name__)

# Sample user data
users = [
    {'username': 'admin', 'role': 'admin'},
    {'username': 'moderator', 'role': 'moderator'},
    {'username': 'user', 'role': 'user'}
]

def get_user(username):
    for user in users:
        if user['username'] == username:
            return user
    return None

@app.route('/welcome/<username>')
def welcome(username):
    user = get_user(username)
    if user:
        role = user['role']
        return render_template("C:\Users\vladp\Desktop\Lab#10\Task#3\Folder\main.html", role=role)
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
