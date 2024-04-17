import qrcode

# The data you want to encode in the QR Code, for example a URL
data = "https://www.example.com"

# Creating a QR Code instance
qr = qrcode.QRCode(
    version=1,  # QR Code version, from 1 to 40, where 1 is the smallest size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code
    border=4,  # Border width around the QR code
)

# Adding data to the QR Code
qr.add_data(data)
qr.make(fit=True)

# Creating an image of the QR Code and saving it
img = qr.make_image(fill='black', back_color='white')
img.save("MyQrCode.png")

print("QR Code generated successfully!")
