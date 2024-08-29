from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
messages = [
]


app = Flask(__name__)
io = SocketIO(app)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', messages=messages)

@io.on('sendMessages')
def receive_message(msg):
    emitted = io.emit('getMessage', msg)
    messages.append(msg)
    

io.run(app, debug=True)