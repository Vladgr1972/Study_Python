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

    def __add__(self, other):
        sum_txt = self.read() + other.read()
        tmp_file_dir = tempfile.gettempdir()
        tmp_file = self.chek_file(os.path.join(tmp_file_dir, self.path_to_file + "_" + other.path_to_file))
        with open(tmp_file,"w",encoding="utf-8") as f:
            f.write(sum_txt)
        return File(tmp_file)

    def __iter__(self):
        self.seek_f = 0
        return self

    def __next__(self):
        file_text = open(self.path_to_file,"r")
        file_text.seek(self.seek_f)
        file_line = file_text.readline()
        self.seek_f = file_text.tell()
        file_text.close()
        if not file_line:
            raise StopIteration
        return file_line



