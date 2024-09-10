from flask import Flask, render_template, request, make_response, redirect, url_for
from flask_socketio import SocketIO, emit
from entry_points.data_entry import Register
import os
messages = [
]

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
io = SocketIO(app)
app.config['SECRET_KEY'] = '23761278361236'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:shirostrongpassword@127.0.0.1:3306/webchat'

@app.route('/home', methods=['GET', 'POST'])
def home():
    if not request.cookies.get('autor'):
        return redirect(url_for('register'))
    return render_template('home.html', messages=messages)



@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = Register()
    
    message = ''
    
    if request.method == 'POST':
        if register_form.validate_on_submit():
            cookie = make_response(redirect(url_for('home')))
            cookie.set_cookie('autor', register_form.name.data)
            cookie.set_cookie('password', register_form.password.data)
            return cookie
        else:
            message = f'Algum erro aconteceu durante o seu registro.'
            print(register_form.password.data)
            print(register_form.repeat_password.data)
    
    return render_template('login.html', register_form=register_form, message=message)

@io.on('sendMessages')
def receive_message(msg):
    emitted = io.emit('getMessage', msg)
    messages.append(msg)



@io.on('clearMessages')
def clear_messages():
    messages.clear()
    emit('clearMessages')
    

io.run(app, debug=True)