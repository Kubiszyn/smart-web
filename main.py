from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import smtplib
import os

app = Flask(__name__)
app.secret_key = 'secret'
app.config['MAIL_SERVER']='poczta.interia.pl'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'testweb123@interia.pl'
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'description' in request.form:
        name = str(request.form['name'])
        email = str(request.form['email'])
        description = str(request.form['description'])
        msg = Message(
                'Hello',
                sender ='testweb123@interia.pl',
                recipients = ['#']
               )
        msg.body = description
        mail.send(msg)
    else:
        return render_template('contact.html')

@app.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

@app.route('/package', methods=['GET', 'POST'])
def package():
    msg = 'None'
    if request.method == 'POST' and 'kilograms' in request.form:
        msg = 'none'
        kg = int(request.form['kilograms'])
        if kg < int(1): 
            msg = '15.90 PLN'
            return render_template('package.html', msg=msg)
        elif kg >= int(1) and kg < int(5): 
            msg = '19.90'
            return render_template('package.html', msg=msg)
        elif kg >= int(5) and kg < int(15) : 
            msg = '20.90'
            return render_template('package.html', msg=msg)
        elif kg >= int(15) and kg < int(31) : 
            msg = '22.90'
            return render_template('package.html', msg=msg)
        elif kg == int(31): 
            msg = '24.90 '
            return render_template('package.html', msg=msg)
        elif kg > int(31):
            overprice  = kg - 31
            msg = (overprice * 1.50) + 24.90
            return render_template('package.html', msg=msg)
    else:
        return render_template('package.html', msg=msg)

@app.route('/buysell', methods=['GET', 'POST'])
def buysell():
    return render_template('buysell.html')

app.run(host='127.0.0.1', port=8000, debug=True)