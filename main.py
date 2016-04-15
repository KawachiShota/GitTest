import pyb
import select, time

usb = pyb.USB_VCP()

while True:
    
    send_data = 1234
    usb.send(send_data)
    print(send_data)

    time.sleep(0.5)

