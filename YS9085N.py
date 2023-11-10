#connect UART pins to TX/RX pins on SSDs board, supports only part number SKF7A 

import serial, rice
from rice import usb.usb2

d = "/tty/usbserial-14A40"
if not usb2(d).c_edit(0x1, 1):
    usb2(d).c_reset(0xffffffff)
# reset if stucks

# 🍄 Some story 🍄 #
#recently (~05.11.23) i tried to open my 7z/rar/tgz archives but i got many CRC-errors. Half of my files are fucked, i like a naive fool trusted to chinese ssd and store all sensitive data on it. 
#Ever never trust your important data to SSDs with Yeestor and some SMI controllers (YS9082HP/YS9082HC/YS9083XT/YS9085N) (SM2258XT (PCIe)/SM2258)
#i still continue to try pull my files, but internal nand corruption.., naaaaahh(((((

#F3 19 C0 FC B2 63 60 07 6A EF B0 70 B7 45 D2 C6 04 4B 37 61 9D FA 56 F7 7F 4D 98 BC 5D CF A8 DB A7 67 F0 0D 48 26
#00 00 23 24 25 26 27 28 29 2A 2B 2C 00 00 00 00 00 00 00
NAND = {
    "parts": {
        0x00: "silly dumby eblan",
        0x23: "Micron",
        0x24: "Intel",
        0x27: "?", # ~ to 23, maybe Spectek
        0x34: "Hynix", 
        0x35: "?", # onfi??? what???
        0xFF: "silly dumby eblan"
    },

    "alg": {
        0x30: "SLC",
        0x32: "MLC",
        0x34: "TLC",
        0x36: "QLC",
        0x38: "?"
    }

    

}



with serial.Serial('/tty/usbserial-14A40', 230400, timeout=10) as s:
    #00 00 00 00 00 00
    #AE

    # sub_A4FEC
    jumpdebug_c = "FF00FF00" + "00001CED" # 1C ED
    selftest_c =  "FF00FF00" + "0000000C"
    selfsmart_c = "FF00FF00" + "0000000D"

    s.write(bytes.fromhex("0000FF00"))

    if s.read(1).hex() == "ae": #jumped
        pass
        
#todo
