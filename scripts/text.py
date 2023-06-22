import segno
import os

# create a qr code with a URL string
qrcode = segno.make('https://news.google.com')
# choose a name for the output file
filename = 'url.png'
# choose an output directory
output_path = '../output/'
# create the QR code image (scaling applied since default is very small)
qrcode.save(f'{output_path}{filename}', scale=7)

# check if file was successfully saved in local directory
if filename in os.listdir(output_path):
    print(f'QR code saved in \"output\" directory as \"{filename}\"')
else:
    print(f'ERROR: QR code not saved to local directory')
