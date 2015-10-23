__author_ = "Gangadhar Mylapuram"
import os
def rename_files():
    dir="C:\\prank"
    saved_path =  os.getcwd();
    print ("Current working dir" + saved_path)
    os.chdir(dir)
    file_list= os.listdir()
    for file_name in file_list:
        new_file_name = file_name.translate(file_name.maketrans("", "", "0123456789"))
        os.rename(file_name, new_file_name)
        #        printf("Failed to rename a file" + file_name);
    os.chdir(saved_path)


if (__name__ == "__main__"):
    rename_files();
