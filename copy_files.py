import os
import shutil
from os import walk
import distutils.core

f = []
# Give correct folder name where you download and unzip text file folder
folder_path = '/Users/Target_Folder'
# Read all text files in a folder - 
for (dir_path, dir_names, text_file_names) in walk(folder_path):
	f.extend(text_file_names)
	break
print("Files to be copied: ")
print(text_file_names)

# Create only parent folder, where you want to copy filtered images. Like here I created "Filter" folder
destination_folder = '/Users/destination_folder'
# Access to your hard drive where all images are there.
# Try reaching to your hard disk using terminal first. So that you'll get correct path
external_disk_path_from_copy = '/Volumes/My Passport/XXXX/'
img_file_name_list = []

for text_file in text_file_names:
	if text_file.endswith(".txt"):
		# Extract folder from text file (Make sure the folder name matches from hard disk)
		folder_name = text_file.replace(' ', ' ')[:-4]
		print("Copying from folder: " + external_disk_path_from_copy + folder_name)
		# Read a text file to get image values
		with open(folder_path+ '/' +text_file) as f:
			img_file_name_list = f.read().split('\n')
		for img_file in img_file_name_list:
			full_image_file_to_copy = os.path.join(external_disk_path_from_copy + folder_name, img_file)
			if(os.path.isfile(full_image_file_to_copy)):
				print("Copying files")
				#print(destination_folder+'/'+folder_name+'/'+img_file)
				if not os.path.exists(destination_folder+'/'+folder_name):
					os.makedirs(destination_folder+'/'+folder_name)
				shutil.copy(full_image_file_to_copy, destination_folder+'/'+folder_name+'/'+img_file)