#!/usr/bin/env python
# Author : Abhinav

import os
from os import path
import shutil
import sys

class Organizer:

    def __init__(self, dir):
        self.dir = dir
        self.directories = ['images','docs','audio','videos','misc']
        self.directory_association = {
            'images': ['jpg','png','svg','jpeg']
            , 'docs': ['pdf', 'odt', 'doc', 'docx', 'xls']
            , 'audio': ['mp3']
            , 'videos': ['mp4']
        }
        

    def setup(self):
        print("Changing to dir %s"%(self.dir))
        os.chdir(self.dir)
        for directory in self.directories:
            if not os.path.isdir(directory):
                os.mkdir(directory)


    def move(self):
        print("Moving all the files into the respective directory")
        with os.scandir() as it:
            for entry in it:
                if entry.is_file():
                    filename, ext = path.splitext(entry)
                    print('Moving %s with extensinon %s'%(filename, ext) )
                    for k,v in self.directory_association.items():
                        if ext.replace('.','') in v:
                            print(ext, v, entry.name)
                            shutil.move(entry.name, k)
                        else:
                            shutil.move(entry.name, 'misc')
                            break
                        

if __name__=='__main__':
    directory_name = sys.argv[1]
    organizer = Organizer(directory_name)
    organizer.setup()
    organizer.move()
