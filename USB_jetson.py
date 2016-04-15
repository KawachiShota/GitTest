import serial, time

ser = serial.Serial("/dev/ttyACM0")
#ser = serial.Serial("/dev/ttyS3")


while True:

    x = ser.readline()
    #print_data  = int(x)
    print type(x)
    print x
    time.sleep(0.5)
