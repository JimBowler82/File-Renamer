import os
from tkinter import *
from  tkinter import filedialog

root = Tk()
root_directory = filedialog.askdirectory()
print (root_directory)

os.chdir(root_directory)

f_new_name = input('Enter desired filename for each entry:')

for idx, f in enumerate(os.listdir(), start=1):
  f_name, f_ext = os.path.splitext(f)
  if f_ext == '.jpg' or f_ext == '.png':
    f_idx = '- ' + str(idx)
    new_name = '{} {}{}'.format(f_new_name, f_idx, f_ext)
    os.rename(f, new_name)
    print(new_name)
  
