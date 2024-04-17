
# QR Code Generator

This Python script allows you to create an image file containing a QR Code generated from a URL specified by the user.

## Dependencies

This script requires the `qrcode` library. You can install this dependency using pip:

```bash
pip install qrcode[pil]
```

## Usage

1. Modify the `data` variable in the script to include the URL or data you want to encode in the QR Code.
2. Run the script with Python to generate the QR Code image:

```bash
python generate_qr.py
```

The image file `MyQrCode.png` will be created in the current directory.

## Configuration

The script is configured with the following parameters:
- `version=1`: This sets the QR Code version, with possible values from 1 to 40. Version 1 is the smallest size.
- `error_correction=qrcode.constants.ERROR_CORRECT_L`: Low error correction level, allows for correction of about 7% of errors.
- `box_size=10`: Defines the size of each box in the QR Code.
- `border=4`: Defines the width of the border around the QR Code.

## Output

The script will save the generated QR Code as the file `myqr.png` in the directory where the script is executed. A message will also be displayed in the console to indicate that the QR Code was generated successfully.

## License

This project is open-source. You can redistribute and/or modify it under the terms of your choice.
