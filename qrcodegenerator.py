import qrcode 
from PIL import Image
print("Qr Code Generator:")
qr = qrcode.QRCode(version=1,box_size=15,border=5)
link = input("Enter the link:")
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color='white')
img.save('QRCode.png')
im = Image.open(r"C:\users\om409\Documents\Code\QRCode.png")  
im.show()  
img = input("You will be able to find the image in the parent directory of this file.")