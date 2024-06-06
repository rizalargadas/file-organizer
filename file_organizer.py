import shutil
import os

IMAGE_FORMATS = ['.jpg', '.jpeg', '.png',
                 '.gif', '.bmp', '.tif', '.tiff', '.svg']
VIDEO_FORMATS = ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv']
DOCUMENT_FORMATS = ['.pdf', '.doc', '.docx', '.ppt',
                    '.pptx', '.xls', '.xlsx', '.txt', '.rtf']
AUDIO_FORMATS = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a']

file_dir = input("Enter directory: ")
file_dir_contents = os.listdir(file_dir)
organized_dirs = ['Images', 'Videos', 'Documents', 'Audios', 'Others']

for dir in organized_dirs:
    if dir not in file_dir_contents:
        os.makedirs(file_dir + '/' + dir)

num_of_moved_images = 0
num_of_moved_videos = 0
num_of_moved_documents = 0
num_of_moved_audios = 0
num_of_moved_others = 0

for f in file_dir_contents:
    file_name_list = f.split('.')
    file_type = '.' + file_name_list[-1]
    source = f'{file_dir}/{f}'

    if os.path.isfile(source):

        if file_type in IMAGE_FORMATS:
            destination = f'{file_dir}/{organized_dirs[0]}/{f}'
            shutil.move(source, destination)
            num_of_moved_images += 1

        elif file_type in VIDEO_FORMATS:
            destination = f'{file_dir}/{organized_dirs[1]}/{f}'
            shutil.move(source, destination)
            num_of_moved_videos += 1

        elif file_type in DOCUMENT_FORMATS:
            destination = f'{file_dir}/{organized_dirs[2]}/{f}'
            shutil.move(source, destination)
            num_of_moved_documents += 1

        elif file_type in AUDIO_FORMATS:
            destination = f'{file_dir}/{organized_dirs[3]}/{f}'
            shutil.move(source, destination)
            num_of_moved_audios += 1

        else:
            destination = f'{file_dir}/{organized_dirs[-1]}/{f}'
            shutil.move(source, destination)
            num_of_moved_others += 1

    elif os.path.isdir(source):
        if f not in organized_dirs:
            destination = f'{file_dir}/{organized_dirs[-1]}/{f}'
            shutil.move(source, destination)
            num_of_moved_others += 1


print(f'{num_of_moved_images} files are successfuly moved to "Images"')
print(f'{num_of_moved_videos} files are successfuly moved to "Videos"')
print(f'{num_of_moved_documents} files are successfuly moved to "Documents"')
print(f'{num_of_moved_audios} files are successfuly moved to "Audios"')
print(f'{num_of_moved_others} files are successfuly moved to "Others"')
