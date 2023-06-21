import segno
import os

# create a qr code with a URL string
qrcode = segno.make('https://news.google.com')
# choose a name for the output file
filename = 'url.png'
# create the QR code image (scaling applied since default is very small)
qrcode.save(filename, scale=7)

# check if file was successfully saved in local directory
if filename in os.listdir(os.getcwd()):
    print(f'QR code saved to \"{filename}\"')
else:
    print(f'ERROR: QR code not saved to local directory')
