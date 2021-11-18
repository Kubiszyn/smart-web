from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

app.run(host='127.0.0.1', port=8000, debug=True)