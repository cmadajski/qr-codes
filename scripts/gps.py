import segno
import os
from segno import helpers

# set latitude and longitude for location
latitude, longitude = 35.000000, -80.000000
# create QR code
qrcode = helpers.make_geo(latitude, longitude)
# set output filename
filename = 'geo.png'
output_path = '../output/'
# save QR code as img (scale up because default is very small)
qrcode.save(f'{output_path}{filename}', scale=7)

# check if QR code img exists in local directory
if filename in os.listdir(output_path):
    print(f'QR code saved in \"output\" directory as \"{filename}\"')
else:
    print('ERROR: QR code not found in local directory')
