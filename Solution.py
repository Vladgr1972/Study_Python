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
        return len(string)



    def chek_file(self,path_to_file):
        self.path_to_file = path_to_file;
        if os.path.exists(self.path_to_file):
            pass
        else:
            open(self.path_to_file,"x")
        return self.path_to_file


    def __str__(self):
        return  os.path.abspath(self.path_to_file)


file_name = "text"

print(os.path.exists(file_name + "_1"))
file_obj_1 = File(file_name + "_1")
print(os.path.exists(file_name + "_1"))
file_obj_2 = File(file_name + "_2")
print(file_obj_1.write('trhyrtrth'))
print(file_obj_1)
print(file_obj_1.read())
print(file_obj_2.write('l55y5'))
print(file_obj_2)
print(file_obj_2.read())
