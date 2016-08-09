import serial
import syslog
import time
#sketch_aug06c
ser = serial.Serial('/dev/cu.usbmodem1421', 9600, timeout=5)
time.sleep(2)
connected = True
i = 0

while (i < 4):
    # Serial write section

    setTempCar1 = 63
    setTempCar2 = 37
    ser.flush()
    setTemp1 = str(setTempCar1)
    setTemp2 = str(setTempCar2)
    print ("Python value sent: ")
    print (setTemp1)
    ser.write(setTemp1)
    time.sleep(1) # I shortened this to match the new value in your Arduino code

    # Serial read section
    msg = ser.read(ser.inWaiting()) # read all characters in buffer
    print ("Message from arduino: ")
    print (msg)
    i = i + 1
else:
    print "Exiting"
exit()
