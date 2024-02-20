#Simple program handling the file and directory deletion.
#author: danielCodingGuy

import os
import shutil

path = 'file.txt'

try:
    #os.remove(path) You can delete the specific file using this function.
    #os.rdir(path)  You can also delete whole directory using this function as long as its empty.
    shutil.rmtree(path) # You can delete whole directory with files inside it using this function.
except FileNotFoundError:
    print('Cannot find the file.')
except PermissionError:
    print('You do not have permission to delete that file.')
except OSError:
    print("You cannot delete that file using this function.")
else:
    print(path + 'file was successfully deleted.')
