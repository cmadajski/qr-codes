# QR Code Generation with Python

QR codes are a similar idea to barcodes, but extended in 2 dimensions. This allows them to hold a decent amount of data in a relatively small form factor. They are especially useful in modern times since both Apple and Google support QR code reading in their default camera apps for phones. People can quickly scan a QR code and process many types of data with reduced effort on their part.

Some of the main applications of QR codes:

- sharing text and URLs
- sharing Wifi login information
- sharing contact info
- sharing GPS coordinates

## Dependencies

There are only 3 dependencies for this project:

1. Python 3.11
2. [Segno](https://segno.readthedocs.io/en/latest/)
3. [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation)

## Installation

Clone the repo to your local system:

`git clone https://github.com/cmadajski/qr-codes.git`

Run the setup script if you are on Linux or MacOS (if you are using Windows, please reconsider your poor decisions and repent). You may need to allow execution privileges before running the script:

```bash
sudo chmod +x setup.sh
source setup.sh
```

Run the main script to actually generate the QR code. The only required argument is the type of QR code being created (text, wifi, mecard, or gps).

```bash
python3 generate_qr.py text
```

There are a number of useful command line options that can be used to increase efficiency and customize QR code output:

```bash
# set a custom scale value (default is 7)
python3 generate_qr.py -s 12 text
# set a custom filepath for the output QR code, includes a custom filename
python3 generate_qr.py -f "~/Downloads/mydata.png" mecard
# read QR code data from a YAML config file
python3 generate_qr.py -c "~/Code/configs/mydata.yaml" gps
```
