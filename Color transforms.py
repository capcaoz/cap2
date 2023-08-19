from PIL import Image

with Image.open("hopper.ppm") as im:
    im = im.convert("L")
