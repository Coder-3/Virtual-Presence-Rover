from flask import Flask, render_template, request, redirect, url_for, make_response
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import motors
import socket

# Ensures device is stopped when starting the app
motors.stop()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
# Optain localhost ip
server_ip = s.getsockname()[0]
s.close()

app = Flask(__name__) 

@app.route('/')

# Specify the HTML template and the ip to access it
def index():
    return render_template('index.html', server_ip=server_ip)

# Tells Flask what URL should trigger the function
@app.route('/<changepin>', methods=['POST'])

# Function to call different motors functions based on return value from the button clicks
def reroute(changepin):

    changePin = int(changepin) 

    if changePin == 1:
        motors.left()
    elif changePin == 2:
        motors.reverse()
    elif changePin == 3:
        motors.right()
    elif changePin == 4:
        motors.forward()
    elif changePin == 5:
        motors.stop()
    else:
        print("Wrong command")

    response = make_response(redirect(url_for('index')))
    return(response)

app.run(debug=True, host=server_ip, port=8000) 

