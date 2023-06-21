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
# save QR code as PNG (scale increased since default is very small)
qrcode.save(filename, scale=7)

# check if QR code file exists in local directory
if filename in os.listdir(os.getcwd()):
    print(f'QR code saved as \"{filename}\"')
else:
    print('ERROR: QR code not found in local directory')
