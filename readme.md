# Make Arduino Dice Robot
Arduino controlling servo motor with dice animating web app

## What you need in things
1. Arduino inventor kit (available in Amazon, Sparkfun)
  * Arduino Uno
  * Servo motor
  * Small jumper cable
  * Breadboard

2. Cardboard, Stick for arm

3. Computer to run a webserver

## S/W
1. virtualenv for Python environment setup
2. Code from this repo

## How to install S/W and Run
1. Create a virtualenv (For more info, go to http://virtualenv.org)
2. In the newly created virtualenv env (meaning after source $env_folder$/bin/activate), git clone https://github.com/imju/dice_arduino.git
3. Run 'pip install requirements.txt' to install Flask and PySerial
4. Open Arduino editor for arduino/servo.ino and upload to arduino (Note down the port!)
5. Update port information in move.py in the following line with your port
  * ser = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=5)
6. python hello.py
7. Go to http://127.0.0.1:5000
8. Have fun! ( Currently only supports single dice up to 6 digits)



Credit: Dice program is from Anton Natarov for details http://www.teall.info/2014/01/online-3d-dice-roller.html
