from flask import Flask, render_template
from motorcontrol import motor_up, motor_down

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('homepage.html')


@app.route('/up')
def up():
    motor_up()
    return {
        'success': 'true'
    }


@app.route('/down')
def down():
    motor_down()
    return {
        'success': 'true'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
