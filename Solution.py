import os
import tempfile

class File:
    def __init__(self,path_to_file):
        self.path_to_file = self.chek_file(path_to_file)

    def read(self,path_to_file):
        pass

    def write(self,path_to_file):
        pass

    def chek_file(self,path_to_file):
        self.path_to_file = path_to_file;
        if os.path.exists(file_name):
            pass
        else:
            open(file_name,"x")
        return path_to_file

    def __str__(self):
        return  self.path_to_file


file_name = "text.tmp"
file_obj = File(file_name)
print(os.path.exists(file_name))
print(file_obj)

