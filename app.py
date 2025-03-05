from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    return redirect(url_for('success', username=username))

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)