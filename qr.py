# Before running, install the required library: pip install qrcode

import qrcode
from pathlib import Path
from datetime import datetime

# Data to encode in the QR code (e.g., a website link, text, etc.)
data_to_encode = "Information you want QR code to store"

# Create a unique filename using the current timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"qr_{timestamp}.png"


# This creates a path to C:\Users\YourName\Downloads\qr_...png (on Windows)
downloads_dir = Path.home() / "Downloads"
# Ensure the Downloads directory exists before saving
downloads_dir.mkdir(exist_ok=True)
save_path = downloads_dir / filename

# Generate the QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)
qr.add_data(data_to_encode)
qr.make(fit=True)

# Create an image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
img.save(save_path)

print(f"QR Code saved successfully to your Downloads folder: {save_path}")
