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
