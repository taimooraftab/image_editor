import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

#to check that directories are selected
print(image_folder,output_folder)

#to check if output_folder exists
os.path.exists(output_folder)

#if it doesn't exist. make new folder
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}.\\{filename}')
	img.save(f'{output_folder}.\\{filename}', '.png')
	print('all done')
