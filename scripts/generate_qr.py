import segno
from segno import helpers
import os
import argparse
import yaml

def create_qr_code(data: dict, qr_type: str = 'text', output_path: str = '../output/qrcode.png', scale: int = 7):
    if qr_type == 'text':
        qrcode = segno.make(data['text'])
    elif qr_type == 'wifi':
        qrcode = helpers.make_wifi(ssid=data['ssid'], password=data['password'], security=data['security'])
    elif qr_type == 'mecard':
        qrcode = helpers.make_mecard(name=f"{data['lastname']}, {data['firstname']}", email=data['email'], phone=data['phone'])
    elif qr_type == 'gps':
        qrcode = helpers.make_geo(lat=data['latitude'], lng=data['longitude'])
    else:
        print('ERROR: QR type not supported.')
    qrcode.save(output_path, scale=scale)

def get_qr_data(qr_type: str) -> dict:
    input_data = dict()
    if qr_type == 'text':
        input_data['text'] = input('Enter text or URL: ')
    elif qr_type == 'wifi':
        input_data['ssid'] = input('Enter the Wifi SSID: ')
        input_data['password'] = input('Enter the Wifi password: ')
        input_data['security'] = input('Enter security type (WPA or WEP): ')
    elif qr_type == 'mecard':
        input_data['firstname'] = input('Enter contact firstname: ')
        input_data['lastname'] = input('Enter contact lastname: ')
        input_data['email'] = input('Enter contact email: ')
        input_data['phone'] = input('Enter contact phone number (+12223334444): ')
    elif qr_type == 'gps':
        geo_info = input('Enter geo data (<latitude> <longitude>): ')
        geo_info_split = geo_info.split(' ')
        input_data['latitude'] = geo_info_split[0]
        input_data['longitude'] = geo_info_split[1]
    return input_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('qr_type', help='type of QR code [text, wifi, mecard, gps]')
    parser.add_argument('-c', '--config', help='read data from YAML config file')
    parser.add_argument('-f', '--filepath', help='filepath for the output QR code image')
    parser.add_argument('-s', '--scale', help='scale the output image size (7 is ideal)', type=int)
    args = parser.parse_args()

    data = dict()

    if args.config:
        with open(args.config) as yaml_data:
            data = yaml.safe_load(yaml_data)
    else:
        data = get_qr_data(args.qr_type)
    
    if args.filepath and args.scale:
        create_qr_code(data, args.qr_type, output_path=args.filepath, scale=args.scale)
    elif args.filepath:
        create_qr_code(data, args.qr_type, output_path=args.filepath)
    elif args.scale:
        create_qr_code(data, args.qr_type, scale=args.scale)
    else:
        create_qr_code(data, args.qr_type)