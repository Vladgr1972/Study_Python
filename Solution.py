import os
import tempfile


class File:
    def __init__(self,path_to_file):
        self.path_to_file = self.chek_file(path_to_file)

    def read(self):
        """ reading data from file """
        if os.path.isfile(self.path_to_file):
            with open(self.path_to_file, "r",encoding="utf-8") as f:
                text = f.read()
        else:
            text = ""
        return text

    def write(self,string):
        """ writing data to file """
        if os.path.isfile(self.path_to_file):
            with open(self.path_to_file, "w",encoding="utf-8") as f:
                f.write(string)
        return len(string)

    def chek_file(self,path_to_file):
        """ checking for files with the file name path_to_file """
        if os.path.exists(path_to_file):
            pass
        else:
            open(path_to_file,"x")
        return path_to_file

    def __str__(self):
        return  os.path.abspath(self.path_to_file)

    def __add__(self, other):
        sum_txt = self.read() + other.read() #reading data from suming objects
        tmp_file_dir = tempfile.gettempdir()
        tmp_file = tempfile.NamedTemporaryFile() # create tmp - file
        tmp_file = self.chek_file(tmp_file.name)
        with open(tmp_file,"w",encoding="utf-8") as f:
            f.write(sum_txt)
        return File(tmp_file)

    def __iter__(self):
        self.seek_f = 0 # seek of file
        return self

    def __next__(self):
        file_text = open(self.path_to_file,"r")
        file_text.seek(self.seek_f) # stand seek of file
        file_line = file_text.readline()
        self.seek_f = file_text.tell() # taking seek of file
        file_text.close()
        if not file_line:
            raise StopIteration
        return file_line

if __name__ == '__main__':
    pass


"""
path_to_file = 'some_filename'

os.path.exists(path_to_file)

file_obj = File(path_to_file)
os.path.exists(path_to_file)

print(file_obj)

file_obj.read()

file_obj.write('some text')

file_obj.read()

file_obj.write('other text')

file_obj.read()

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
file_obj_1.write('line 1\n')

file_obj_2.write('line 2\n')

new_file_obj = file_obj_1 + file_obj_2
isinstance(new_file_obj, File)

print(new_file_obj)

for line in new_file_obj:
    print(ascii(line))

new_path_to_file = str(new_file_obj)
os.path.exists(new_path_to_file)

file_obj_3 = File(new_path_to_file)

print("3 > ", file_obj_3)
print("1 > ",file_obj_1)
print("2 > ",file_obj_2)
print("new > ",new_file_obj)

"""
