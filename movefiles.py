import os
import shutil
import time

# Ask where these files are
print('Where are the files you wish to be sorted located? (write the full directory)')

chosenDirectory = input('Enter it here: ')
os.chdir(chosenDirectory)


# Ask and assign what type of file should be moved (image,exe, xsls, docx etc.)

print('What type of files do you want to move?\nPlease type: \n1) Image file\n2) TXT file\n3) Audio file\n4) Excel file\n5) Program files ')

fileDecision = int(input('Enter one of the numbers: '))

print('What do you want the folder that all the files are in called?')
fileName = input('Enter the name here: ')
print('Thanks! Preparing to sort the files...')
time.sleep(3)

# Functions
def checkPicture():
    os.chdir(chosenDirectory) # changes directory to the one chosen
    os.makedirs(fileName) # creates a folder with name fileName
    
    chosenDestination =  os.path.join(os.getcwd(), fileName) # joins directory with images
    filelist = os.listdir()
    filelist = [files.upper() for files in filelist] # converts everything to uppercase for faster comparisons
    
    
    for file in filelist:
        
        os.chdir(os.path.dirname(__file__)) # changes directory to the one where the py file is located
        
        with open('formats//image_formats.txt', 'r') as textFormat:
            
            os.chdir(chosenDirectory) # changes directory to chosen directory
           
            for text in textFormat.readlines(): # loop that reads all lines of image_formats.txt

                if os.path.isfile(os.path.join(os.getcwd(), file)) == True:
                    
                    if file.endswith(text.strip()): # if the file ends with any of the formats, enter if statement
                        os.chdir(chosenDirectory) 
                        shutil.move(os.path.join(os.getcwd(), file), chosenDestination) # move file from chosen directory to the chosen destination.
                        print(str(file) + ' is an image file with format ' + text)
                        break
                                  
                    else:
                        print(str(file) + ' is not a match with ' + text)
                else:
                    break
            os.chdir(os.path.dirname(__file__)) # change directory back to py file

  
def checkTXT():
    os.chdir(chosenDirectory) # changes directory to the one chosen
    os.makedirs(fileName) # creates a folder called Images
    
    chosenDestination =  os.path.join(os.getcwd(), fileName) # joins directory with images
    filelist = os.listdir()
    filelist = [files.upper() for files in filelist] # converts everything to uppercase for faster comparisons
    
    
    for file in filelist:
        
        os.chdir(os.path.dirname(__file__)) # changes directory to the one where the py file is located
        
        with open('formats//word_formats.txt', 'r') as textFormat:
            
            os.chdir(chosenDirectory) # changes directory to chosen directory
           
            for text in textFormat.readlines(): # loop that reads all lines of image_formats.txt

                if os.path.isfile(os.path.join(os.getcwd(), file)) == True:
                    
                    if file.endswith(text.strip()): # if the file ends with any of the formats, enter if statement
                        os.chdir(chosenDirectory) 
                        shutil.move(os.path.join(os.getcwd(), file), chosenDestination) # move file from chosen directory to the chosen destination.
                        print(str(file) + ' is a word processing file with format ' + text)
                        break
                                  
                    else:
                        print(str(file) + ' is not a word processing file with ' + text)
                else:
                    break
            os.chdir(os.path.dirname(__file__)) # change directory back to py file

def checkAudio():
    os.chdir(chosenDirectory) # changes directory to the one chosen
    os.makedirs(fileName) # creates a folder called Images
    
    chosenDestination =  os.path.join(os.getcwd(), fileName) # joins directory with images
    filelist = os.listdir()
    filelist = [files.upper() for files in filelist] # converts everything to uppercase for faster comparisons
    
    
    for file in filelist:
        
        os.chdir(os.path.dirname(__file__)) # changes directory to the one where the py file is located
        
        with open('formats//audio_formats.txt', 'r') as textFormat:
            
            os.chdir(chosenDirectory) # changes directory to chosen directory
           
            for text in textFormat.readlines(): # loop that reads all lines of image_formats.txt

                if os.path.isfile(os.path.join(os.getcwd(), file)) == True:
                    
                    if file.endswith(text.strip()): # if the file ends with any of the formats, enter if statement
                        os.chdir(chosenDirectory) 
                        shutil.move(os.path.join(os.getcwd(), file), chosenDestination) # move file from chosen directory to the chosen destination.
                        print(str(file) + ' is a audio file with format ' + text)
                        break
                                  
                    else:
                        print(str(file) + ' is not an audio file with ' + text)
                else:
                    break
            os.chdir(os.path.dirname(__file__)) # change directory back to py file  
# If statements
if fileDecision == 1:
    checkPicture()
    print('Done! All files have been moved to a folder called ' + fileName + ' located in your selected directory!')

elif fileDecision == 2:
    checkTXT()
    print('Done! All files have been moved to a folder called ' + fileName +  'located in your selected directory!')
elif fileDecision == 3:
    checkAudio()
    print('Done! All files have been moved to a folder called ' + fileName +  'located in your selected directory!')

