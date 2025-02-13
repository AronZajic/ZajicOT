from PIL import Image

# Open the image
image = Image.open("resources/textures/key/key-blue.png")  # Replace with your image filename

# Split horizontally into 12 parts (32x32)
for i in range(12):
    cropped_image = image.crop((i * 32, 0, (i + 1) * 32, 32))
    cropped_image.save(f"resources/textures/key/{i + 1}.png")  # Save each part as a separate file
