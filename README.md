# QR Code Generation with Python

QR codes are a similar idea to barcodes, but extended in 2 dimensions. This allows them to hold a decent amount of data in a relatively small form factor. They are especially useful in modern times since both Apple and Google support QR code reading in their default camera apps for phones. People can quickly scan a QR code and process many types of data with reduced effort on their part.

Some of the main applications of QR codes:

- sharing text and URLs
- sharing Wifi login information
- sharing contact info
- sharing GPS coordinates

## Libraries

All the QR generation in this repo is powered by **Python 3.11** and the **Segno** module. Segno seems to be the best QR code library available [based on these stats](https://segno.readthedocs.io/en/latest/comparison-qrcode-libs.html). I've tested all of the various QR code styles and they work on all the hardware I currently have available. It is awesome.

Segno has [extensive documentation](https://segno.readthedocs.io/en/latest/make.html) that explains the details of the package.
