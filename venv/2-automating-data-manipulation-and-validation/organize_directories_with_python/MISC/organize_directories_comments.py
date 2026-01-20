# This library contains func's that interacts with my OS:
import os
# Import the Path func from the pathlib library.
from pathlib import Path

# Obj maps four basic categories, two lists of specific file types.  
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

# If func encounters a suffix that doesn't correspond to the four categories defined above, then return a fifth category `MISC` to represent miscellaneous.
# For-loop to iterate through items in the directory depending on the  file suffix
def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            return category
    return "MISC"

# test out the `pickDirectory()` function.
print(pickDirectory(".pdf"))

# Iterate through each file within the working dir.
def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        # If the directory that the file maps to already exists, a file path is created.
        filePath = Path(item)
        # From that, the file type is extracted.
        fileType = filePath.suffix.lower()
        # pickDirectory func that we defined previously is called to assign the correct directory to the current file.
        directory = pickDirectory(fileType)
        # A directory path is created.
        directoryPath = Path(directory)
        # If directory path doesn't already exist, a new directory is created. 
        if directoryPath.is_dir() != True:
            # file path is updated to include the new directory path. Now you can call the
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))

# Call the organizeDirectory() function to test the program.
organizeDirectory()