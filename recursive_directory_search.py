from os import listdir
from os.path import isdir

def txt_file_names(files=listdir('text_files')):
    for i in files:
        if isdir(i):
            print('dir {}'.format(i))
            txt_file_names(listdir('i'))
        elif '.txt' in i:
            yield i

for i in txt_file_names():
    print(i)
            



