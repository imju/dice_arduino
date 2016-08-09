import serial

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

while True:
    if (ser.inWaiting()>0):
        print('!')
        print ser.readline()
