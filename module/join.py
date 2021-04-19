#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

import os
import re
import hashlib
from module import error

class InitializationBinaryJoin:
    directorypath = ''
    number = ''
    filecontents = ''

    def __init__(self, file, num):
        # self.directorypath = file + '*'
        self.directorypath = 'input\/'
        self.number = num
        self.filecontents = file

class BinaryJoin(InitializationBinaryJoin):
    outputpath = ''

    def __init__(self, file, num):
        InitializationBinaryJoin.__init__(self, file, num)
        directorynumber = len([name for name in os.listdir(self.directorypath) if os.path.isfile(os.path.join(self.directorypath, name))])
        self.outputpath = '.\\output\\' + re.sub(r'.*input.', '', self.filecontents)

        try:
            if (directorynumber - 1) < self.number:
                error.raiseMaximumNumberError()

            elif (directorynumber - 1) > self.number:
                error.raiseMinimummNumberError()

        except error.MaximumNumberError:
            error.displayMaximumNumberError()

        except error.MinimummNumberError:
            error.displayMinimummNumberError()

    def joinBinary(self):
        with open(self.filecontents + '.out', 'wb') as output:
            for i in range(self.number):
                with open(self.filecontents + '.div' + str(i), 'rb') as div:
                    output.write(div.read())
        
        self.renameBinary()
    
    def renameBinary(self):
        os.rename(self.filecontents + '.out', self.outputpath)

    def getCheckSum(self):
        with open(self.outputpath, 'rb') as readfile:
            checksum = hashlib.md5(readfile.read()).hexdigest()
            return checksum
    
    def displayResult(self):
        print("")
        print("============================================================")
        print(" Thank you for your patience. The file has been join.")
        print("============================================================")
        print(" Result file          : {}".format(self.outputpath))
        print("------------------------------------------------------------")
        print(" Number of divisions  : {}".format(self.number))
        print("------------------------------------------------------------")
        print(" hash value [ MD5 ]   : {}".format(self.getCheckSum()))
        print("------------------------------------------------------------")
        print(" Merged files")
        print("------------------------------------------------------------")

        for i in range(self.number):
            print(" ----- {}.div{}".format(self.filecontents, i))
            os.remove(self.filecontents + '.div' + str(i))

        print("============================================================")
        print("")

def setup(file, num):
    return BinaryJoin(file, num)
