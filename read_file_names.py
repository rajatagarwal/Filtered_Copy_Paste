from os import walk
from shutil import copyfile

# To get list of files names in the "text" file
f = []
external_disk_path = '/Volumes/My Passport/XXXX'
for (dir_path, dir_names, file_names) in walk(external_disk_path):
	f.extend(file_names)
	break

print("File names to be copied:")
print(file_names)

destination_file = open("/Users/file_name.txt", "w")

for item in file_names:
	destination_file.write(item)
	destination_file.write("\n")
destination_file.close()