from flask import Flask
from motorcontrol import motor_up, motor_down

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/up')
def up():
    motor_up()
    return 'Motor Moved Up!'


@app.route('/down')
def down():
    motor_down()
    return 'Motor Moved Down!'


if __name__ == '__main__':
    app.run()
