import os
import shutil
import time

# Ask where these files are
print('Where are the files you wish to be sorted located? (write the full directory)')

chosenDirectory = input('Enter it here: ')
os.chdir(chosenDirectory)

# Ask and assign what type of file should be moved (image,exe, xsls, docx etc.)

print(
    'What type of files do you want to move?\nPlease type: \n1) Image file\n2) Word processing file\n3) Audio '
    'file\n4) Excel file\n5) Program files ')

fileDecision = int(input('Enter one of the numbers: '))

print('Would you like to:\n1) Create a new folder\n2) Use an existing folder')
fileChoose = int(input('Enter one of the numbers: '))
newFolder = False
# Variables for selection-if statement.
givenFolderDir = ''
fileName = ''
if fileChoose == 1:
    newFolder = True
    print('What do you want the folder that all the files are in called?')
    fileName = input('Enter the name here: ')
elif fileChoose == 2:
    print('What is the full directory of the folder you wish to copy the files to?')
    givenFolderDir = input()
print('Thanks! Preparing to sort the files...')
time.sleep(3)


# Class
class CheckFunctions:
    def __init__(self, formatfile):  # constructor with formatfile
        self.formatfile = formatfile  # defines format file to be initialised later

    def check(self):
        os.chdir(chosenDirectory)  # changes directory to the one chosen
        if newFolder:
            os.makedirs(fileName)  # creates a folder called fileName
            chosendestination = os.path.join(os.getcwd(), fileName)  # joins directory with fileName
        else:
            chosendestination = givenFolderDir
        filelist = os.listdir(chosenDirectory)
        filelist = [files.upper() for files in filelist]  # converts everything to uppercase for faster comparisons

        for file in filelist:

            os.chdir(os.path.dirname(__file__))  # changes directory to the one where the py file is located

            with open(self.formatfile, 'r') as textFormat:  # self.formatfile essentially becomes what was defined in the constructor

                os.chdir(chosenDirectory)  # changes directory to chosen directory

                for text in textFormat.readlines():  # loop that reads all lines of image_formats.txt

                    if os.path.isfile(os.path.join(os.getcwd(), file)):

                        if file.endswith(text.strip()):  # if the file ends with any of the formats, enter if statement
                            os.chdir(chosenDirectory)
                            shutil.move(os.path.join(os.getcwd(), file),
                                        chosendestination)  # move file from chosen directory to the chosen destination.
                            print(str(file) + ' is an image file with format ' + text)
                            break

                        else:
                            print(str(file) + ' is not a match with ' + text)
                    else:
                        break
                os.chdir(os.path.dirname(__file__))  # change directory back to py file


# If statements
if fileDecision == 1:
    calling = CheckFunctions('formats//image_formats.txt')  # initialise the class constructor defining self.formatfile
    calling.check()  # runs the check() function that finishes the job off.
    if newFolder:
        print('Done! All files have been moved to a folder ' + fileName + ' located in your selected directory!')
    else:
        print('Done! All files have been moved to a folder with directory ' + givenFolderDir)

elif fileDecision == 2:
    calling = CheckFunctions('formats//word_formats.txt')  # initialise the class constructor defining self.formatfile
    calling.check()  # runs the check() function that finishes the job off.
    if newFolder:
        print('Done! All files have been moved to a folder ' + fileName + ' located in your selected directory!')
    else:
        print('Done! All files have been moved to a folder with directory ' + givenFolderDir)
elif fileDecision == 3:
    calling = CheckFunctions('formats//audio_formats.txt')  # initialise the class constructor defining self.formatfile
    calling.check()  # runs the check() function that finishes the job off.
    if newFolder:
        print('Done! All files have been moved to a folder ' + fileName + ' located in your selected directory!')
    else:
        print('Done! All files have been moved to a folder with directory ' + givenFolderDir)
elif fileDecision == 4:
    calling = CheckFunctions('formats//excel_formats.txt')  # initialise the class constructor defining self.formatfile
    calling.check()  # runs the check() function that finishes the job off.
    if newFolder:
        print('Done! All files have been moved to a folder ' + fileName + ' located in your selected directory!')
    else:
        print('Done! All files have been moved to a folder with directory ' + givenFolderDir)
