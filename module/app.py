#!/usr/bin/env python3.6
# -*- coding: utf-8 -*
import sys
import os.path

class InitializeTheArgument:
    argsvalues = []

    # 初期化
    def __init__(self):
        self.argsvalues = sys.argv

    # 取得した引数を返す
    def getArgs(self):
        return self.argsvalues

class ProcessingOfArguments(InitializeTheArgument):
    filename = ''

    def __init__(self):
        InitializeTheArgument.__init__(self)
        # self.filename = self.argsvalues[(self.argsvalues.index("-f") + 1)]

    def processBranching(self):
        if '-h' in self.argsvalues:
            self.displayHelp()
        else:
            self.checkTargetPath()
    
    def displayHelp(self):
        print("")
        print(" App name : binary_dc.py Example CLI")
        print(" Author   : S.Murata <satoru070505@gmail.com>")
        print("")
        print(" FLAGS:")
        print("     -h,    Prints help information")
        print("")
        print(" USAGE:")
        print("   Split  : python binary_dc.py [filename]")
        print("   Join   : python binary_dc.py [filename] [num]")
        print("")
        print(" EXAMPLE:")
        print("   Split  : python binary_dc.py xxxxxx.zip")
        print("   Join   : python binary_dc.py xxxxxx.zip x")
        print("")
        sys.exit()
    
    def checkTargetPath(self):
        os.path.exists(self.argsvalues[1])

def setup():
    return ProcessingOfArguments()
