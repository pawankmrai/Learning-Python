import os

def rename_files():
    # get file name from folder
    file_list = os.listdir("/Users/pawan/Documents/Udacity/Python/prank")
    #print (file_list)
    # Change the current directory
    saved_path = os.getcwd()
    #print("Current working directory: " + saved_path)
    os.chdir("/Users/pawan/Documents/Udacity/Python/prank")

    # rename each file name
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(saved_path)

rename_files()
