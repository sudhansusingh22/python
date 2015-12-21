import os

def rename_filesindir():
    #get file names from a folder
    file_list = os.listdir(r"C:\Users\Sudhansu\Desktop\Python\alphabet")
    print(file_list)
    saved_path = os.getcwd()
    print(saved_path)
    os.chdir("C:\Users\Sudhansu\Desktop\Python\prank")
    for each_file in file_list:
        os.rename(each_file , each_file.translate(None, "0123456789"))
rename_filesindir()    
