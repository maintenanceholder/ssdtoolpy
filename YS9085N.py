#connect UART pins to TX/RX pins on SSDs board, supports only part number SKF7A 

import serial, rice
from rice import usb.usb2

d = "/tty/usbserial-14A40"
if not usb2(d).c_edit(0x1, 1):
    usb2(d).c_reset(0xffffffff)
# reset if stucks

with serial.Serial('/tty/usbserial-14A40', 230400, timeout=10) as s:
    #00 00 00 00 00 00
    #AE
    
    s.write(bytes.fromhex("0000FF00"))

    if s.read(1).hex() == "ae": #jumped
        pass
        
#todo
