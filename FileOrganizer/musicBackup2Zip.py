#! pyton3
# This program copies the entire Music folder and its content into
# a ZIP whose filename increments.

import zipfile, os, re

def backupToZip(folder):
    #Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder) # make sure folder is absolute 

    # Figure out the filename this code should use based on 
    # what files already exist 

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    
    # TODO: Create the ZIP file 
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.\n')




if __name__ == "__main__":

    foldername = input("Please enter the path of the folder you want to backup: ")
    if(re.match(r"C:\\\\Users\\izuen\\\w+", foldername)):
        print('backing up :' + foldername + '\n')
        backupToZip(foldername)
    else:
        foldername = 'C:\\\\Users\\izuen\\' + foldername
        print('backing up :' + foldername + '\n')
        backupToZip(foldername)


# ideas to improve 
# - Make gui 
# - make automatic bash function that listens to music folder and backs up 
# after N number of additions to folder 
# - prompts user before backing up 
    


