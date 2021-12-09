import os
import sys
import tempfile



class File:
    def __init__(self,path_to_file):
        self.path_to_file = self.chek_file(path_to_file)


    def read(self):
        if os.path.isfile(self.path_to_file):
            with open(self.path_to_file, "r",encoding="utf-8") as f:
                text = f.read()
        else:
            text = ""
        return text


    def write(self,string):
        if os.path.isfile(self.path_to_file):
            with open(self.path_to_file, "w",encoding="utf-8") as f:
                f.write(string)



    def chek_file(self,path_to_file):
        self.path_to_file = path_to_file;
        if os.path.exists(file_name):
            pass
        else:
            open(file_name,"x")
        return path_to_file


    def __str__(self):
        return  os.path.abspath(self.path_to_file)


file_name = "text.tmp"
file_obj = File(file_name)
print(os.path.exists(file_name))
print(file_obj)
print(file_obj.read())
file_obj.write("Some text")
print(file_obj.read())

