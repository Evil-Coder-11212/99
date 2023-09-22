# importing the required modules
import os
import shutil
import time

def removeFolder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")


def removeFile(path):
	if not os.remove(path):
		print(f"{path} is removed successfully")

def folderAge(path):
	time = os.stat(path).st_ctime
	return time

def main(days, PATH):
	deletedFiles = 0
	deletedFolders = 0
	seconds = time.time() - (days * 24 * 60 * 60)
	if os.path.exists(PATH):
		for root_folder, folders, files in os.walk(PATH):
			if seconds >= folderAge(root_folder):
				removeFolder(root_folder)
				deletedFolders += 1
			else:
				for folder in folders:
					folder_path = os.path.join(root_folder, folder)
					if seconds >= folderAge(folder_path):
						removeFolder(folder_path)
						deletedFolders += 1 
				for file in files:
					file_path = os.path.join(root_folder, file)
					if seconds >= folderAge(file_path):
						removeFile(file_path)
						deletedFiles += 1 
		else:
			if seconds >= folderAge(PATH):
				removeFile({PATH})
				deletedFiles += 1 

	else:
		print(f'"{PATH}" is not found')
		deletedFiles += 1 # incrementing count

	print(f"Total folders deleted: {deletedFolders}")
	print(f"Total files deleted: {deletedFiles}")




if __name__ == '__main__':
	main()