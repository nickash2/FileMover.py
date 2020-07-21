import os
import shutil
import time


# Classes


class CheckValidNumbers:
    def __init__(self, decisionType, listType):
        self.decisionType = decisionType
        self.listType = listType

    def checkValidNo(self):
        while True:
            try:
                self.decisionType = int(input('Enter one of the numbers: '))

                self.listType[
                    # if the number given is too large it goes over the index of the given list so it raises a IndexError
                    self.decisionType - 1]  # Allowing the except statement to be called
                print(type(self.decisionType))
                break
            except (ValueError, IndexError):  # if the value is not a number or the index isn't present in the list
                print(type(self.decisionType))
                print('You have not entered a number, please try again')


class CheckDir:
    def __init__(self, userChosenDir):
        self.userChosenDir = userChosenDir

    def funcDir(self):
        while True:
            try:
                self.userChosenDir = input('Enter it here: ')
                os.chdir(self.userChosenDir)  # changes directory given by the user
                break
            except (FileNotFoundError, OSError):
                print('You have not entered a valid directory, please try again')


class CheckFunctions(CheckDir):
    def __init__(self, formatfile, userChosenDir):  # constructor with formatfile
        super().__init__(userChosenDir)
        self.formatfile = formatfile  # defines format file to be initialised later

    def checkFunc(self):
        os.chdir(self.userChosenDir)  # changes directory to the one chosen

        if createFolder:
            os.makedirs(inputName)  # creates a folder called inputName
            destination = os.path.join(os.getcwd(), inputName)  # joins directory with inputName
        else:
            destination = inputFolderDir
        filelist = os.listdir(self.userChosenDir)
        filelist = [files.upper() for files in filelist]  # converts everything to uppercase for faster comparisons

        for file in filelist:
            if os.path.isfile(os.path.join(os.getcwd(), file)):
                os.chdir(os.path.dirname(__file__))  # changes directory to the one where the py file is located

                with open(self.formatfile,
                          'r') as textFormat:  # self.formatfile essentially becomes what was defined in the constructor

                    os.chdir(self.userChosenDir)  # changes directory to chosen directory

                    for text in textFormat.readlines():  # loop that reads all lines of image_formats.txt
                        if file.endswith(
                                text.strip()):  # if the file ends with any of the formats, enter if statement
                            os.chdir(self.userChosenDir)
                            shutil.move(os.path.join(os.getcwd(), file),
                                        destination)  # move file from chosen directory to the chosen destination.
                            print(str(file) + ' is an image file with format ' + text)
                            break

                        else:
                            print(str(file) + ' is not a match with ' + text)
            else:
                continue
        os.chdir(os.path.dirname(__file__))  # change directory back to py file


# Ask where these files are

print('Where are the files you wish to be sorted located? (write the full directory)')

# Validation that the user enters a valid directory
userInput = 0
dirObj = CheckDir(userInput)  # creates an object with the users input
dirObj.funcDir()  # calls funDir in the CheckDir class
userInput = dirObj.userChosenDir  # assigns the userinput variable to the userchosendir given before.

# Ask and assign what type of file should be moved (image,exe, xsls, docx etc.)

print(
    'What type of files do you want to move?\nPlease type: \n1) Image file\n2) Word processing file\n3) Audio '
    'file\n4) Excel file\n5) Program files ')
validNoList = [1, 2, 3, 4, 5]  # list of valid numbers for the 1st print statement
validNoList2 = [1, 2]  # list of valid numbers for the 2nd print statement

typeDecision = 0
decisionObj = CheckValidNumbers(typeDecision, validNoList)
decisionObj.checkValidNo()
typeDecision = decisionObj.decisionType
# Prompt Options
print('Would you like to:\n1) Create a new folder\n2) Use an existing folder')
fileNoChoose = 0
fileNoObj = CheckValidNumbers(fileNoChoose, validNoList2)
fileNoObj.checkValidNo()
createFolder = False

# Variables for selection-if statement.
inputFolderDir = ''
inputName = ''
fileNoChoose = fileNoObj.decisionType

# If statements
if fileNoChoose == 1:
    createFolder = True
    print('What do you want the folder that all the files are in called?')
    inputName = input('Enter the name here: ')
elif fileNoChoose == 2:
    print('What is the full directory of the folder you wish to copy the files to?')
    inputFolderDir = input()
print('Thanks! Preparing to sort the files...')
time.sleep(3)
choicesList = ['image', 'word', 'audio', 'excel', 'program']

#  Format TXT file objects
calling = CheckFunctions(f'formats//{choicesList[typeDecision - 1]}_formats.txt',
                         userInput)  # initialise the class constructor defining self.formatfile
calling.checkFunc()  # runs the check() function that finishes the job off.
if createFolder:
    print('Done! All files have been moved to a folder ' + inputName + ' located in your selected directory!')
else:
    print('Done! All files have been moved to a folder with directory ' + inputFolderDir)
