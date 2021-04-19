#!/usr/bin/env python3.6
# -*- coding: utf-8 -*
import os
import re
import hashlib

class InitializationBinarySplit:
    size = ''
    length = ''
    numberofdivisions = ''
    lastlength = ''

    def __init__(self, filecontents):
        self.size = 1024*1024*9
        self.length = os.path.getsize(filecontents)
        self.numberofdivisions = round((self.length + self.size - 1) / self.size)
        self.lastlength = (self.size * self.numberofdivisions) - self.length

class BinarySplit(InitializationBinarySplit):
    filecontents = ''
    outputpath = ''

    def __init__(self, file):
        self.filecontents = file
        InitializationBinarySplit.__init__(self, self.filecontents)
        self.outputpath = '.\\output\\' + re.sub(r'.*input.', '', self.filecontents)

    def splitBinary(self):
        with open(self.filecontents, 'rb') as binary:
            for i in range(self.numberofdivisions):
                readseize = self.lastlength if i == self.numberofdivisions -1 else self.size
                date = binary.read(readseize)
                with open(self.outputpath + '.div' + str(i), 'wb') as output:
                    output.write(date)
    
    def getCheckSum(self):
        with open(self.filecontents, 'rb') as readfile:
            checksum = hashlib.md5(readfile.read()).hexdigest()
            return checksum
    
    def displayResult(self):
        print("")
        print("============================================================")
        print(" Thank you for your patience. The file has been split.")
        print("============================================================")
        print(" Original file        : {}".format(self.filecontents))
        print("------------------------------------------------------------")
        print(" Number of divisions  : {}".format(self.numberofdivisions))
        print("------------------------------------------------------------")
        print(" hash value [ MD5 ]   : {}".format(self.getCheckSum()))
        print("------------------------------------------------------------")
        print(" Split files")
        print("------------------------------------------------------------")

        for i in range(self.numberofdivisions):
            print(" +++++ {}.div{}".format(self.outputpath, i))

        print("============================================================")
        print("")

def setup(file):
    return BinarySplit(file)
