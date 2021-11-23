from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

@app.route('/package', methods=['GET', 'POST'])
def package():
    return render_template('package.html')

@app.route('/buysell', methods=['GET', 'POST'])
def buysell():
    return render_template('buysell.html')

app.run(host='127.0.0.1', port=8000, debug=True)