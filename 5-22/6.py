from PIL import Image

image = Image.open('logo.png')
# image.format, image.size, image.mode ('PNG', (500, 750), 'RGB')
# rect = 80, 20, 310, 360
# image.crop(rect).show()
size = 128, 128
image.thumbnail(size)
image.show()