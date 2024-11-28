# install all the libaries needed 
# create a function that collects a text and converts it to a Qr code
# save the qrcode as a image 
# run the function

import qrcode

def generate_qrcode(text):

  qr = qrcode.QRCode( 
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
   )
 
  qr.add_data(text)
  qr.make(fit=True)
  img = qr.make_image(fill_color="Black", back_color="White")
  img.save("giri01.png")



generate_qrcode("Hey guys im Sharan, this is my github account : https://github.com/sharan37600 ")

  
  