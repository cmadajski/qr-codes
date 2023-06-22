import segno
from segno import helpers
import os

# set personal data
firstname = 'John'
lastname = 'Doe'
email = 'johndoe@gmail.com'
phone = '+12342342345'

# create QR code 
qrcode = helpers.make_mecard(name=f'{lastname}, {firstname}', email=email, phone=phone)
# set output filename
filename = 'mecard.png'
output_path = '../output/'
# save QR code as PNG (scale increased since default is very small)
qrcode.save(f'{output_path}{filename}', scale=7)

# check if QR code file exists in local directory
if filename in os.listdir(output_path):
    print(f'QR code saved in \"output\" directory as \"{filename}\"')
else:
    print('ERROR: QR code not found in local directory')
