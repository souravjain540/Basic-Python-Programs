import io

import numpy as np
import rembg
from PIL import Image


class ImageProcessor:
    def __init__(self, input_path: str, output_filename: str):
        self.input_path = input_path
        self.output_filename = output_filename

    def remove_background(self):
        image = Image.open(self.input_path)

        output = rembg.remove(image)

        if isinstance(output, bytes):
            transparent_image = Image.open(io.BytesIO(output))
        elif isinstance(output, np.ndarray):
            transparent_image = Image.fromarray(output)
        elif isinstance(output, Image.Image):
            transparent_image = output
        else:
            raise TypeError(f"Unexpected type from rembg.remove(): {type(output)}")

        # By default I expect output_filename to be {name}.png
        transparent_image = transparent_image.convert("RGB")
        transparent_image.save(self.output_filename)


processor = ImageProcessor(
    input_path="test.jpg", output_filename="removed-background.png"
)
processor.remove_background()
