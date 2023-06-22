import segno
import os
from segno import helpers

# set wifi data
ssid = 'Your Network Here'
wifi_pass = 'supersecretpassword'
# wifi encryption type (either WPA or WEP)
wifi_sec = 'WPA'

# create QR code for Wifi
qrcode = helpers.make_wifi(ssid=ssid, password=wifi_pass, security=wifi_sec)
# set output filename
filename = 'wifi.png'
# save QR code as an image (scale up since default is very small)
qrcode.save(filename, scale=7)

# confirm that QR code is saved in local directory
if filename in os.listdir(os.getcwd()):
    print(f'QR code saved to \"{filename}\"')
else:
    print('ERROR: QR code could not be saved to local directory')
