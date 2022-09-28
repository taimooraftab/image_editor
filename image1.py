from PIL import Image

img = Image.open('bulbasaur.jpg')

print(img)

img.thumbnail((400,400))
img.save('thumbnail.jpg')