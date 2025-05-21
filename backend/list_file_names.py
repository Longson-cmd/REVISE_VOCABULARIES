import os  # Import the os module for interacting with the file system

# Define the path to the folder containing audio sentence files
# Use a raw string (r"...") to avoid issues with backslashes in Windows file paths
folder_path = 'C:/Users/PC/Desktop/Practise/backend/audios/sentences'

# List all entries (files and directories) in the specified folder
file_list = os.listdir(folder_path)

# Filter the list to include only files (exclude directories)
files = [f for f in file_list if os.path.isfile(os.path.join(folder_path, f))]

# Print the list of audio files in the 'sentences' folder
print(files)

# Define the root folder where we want to search for all audio files
root_folder = 'backend/audios'

# Create an empty list to store the full paths of all audio files found
all_files = []

import os

root_folder = 'backend/audios'
all_files = []

for dirpath, dirnames, filenames in os.walk(root_folder):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename) # Result: 'C:/Users/PC/Desktop/Practise/backend/audios/sentences/eat_sentence_1.mp3'
        # Convert full_path to a relative URL-friendly path
        relative_path = os.path.relpath(full_path, root_folder) # Result: 'sentences/eat_sentence_1.mp3'
        # Normalize to use forward slashes (even on Windows)
        web_path = f'audios/{relative_path}'.replace('\\', '/') # Result: 'audios/sentences/eat_sentence_1.mp3'
        all_files.append(web_path)
        # print(full_path)
        # print(relative_path)
        # print(web_path)
        # break
# Example output: ['audios/sentences/eat_sentence_1.mp3', ...]

# Print the list of all audio files in the entire 'audios' folder tree
print(all_files)
# if I want to each file name like '/backend/audios\\words\\eat.mp3


# First iteration:
# dirpath = 'backend/audios'
# dirnames = ['sentences', 'words']
# filenames = []