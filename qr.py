import pyqrcode
import png
from pyqrcode import QRCode
  
# String which represent the QR code 
s = "http://surl.li/gymbd"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png"
url.png("git.png", scale = 6)

