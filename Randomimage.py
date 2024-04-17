from PIL import Image, ImageDraw
import random

def generate_random_image(width, height):
    # Create a new image with white background
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # Generate random pixels
    for x in range(width):
        for y in range(height):
            # Generate random RGB values
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = (r, g, b)
            draw.point((x, y), fill=color)

    return image

if __name__ == "__main__":
    # Define image dimensions
    width = 400
    height = 400

    # Seed the random number generator with a different value each time
    random.seed()

    # Generate random image
    random_image = generate_random_image(width, height)

    # Save image
    random_image.save("random_image.png")

    # Display image
    random_image.show()
