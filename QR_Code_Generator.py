import qrcode

msg = "Hello World"
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=3,
)
qr.add_data(msg)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QRcode.png")
