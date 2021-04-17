#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

# ////////////////////////////////////////////////////////////////////////// #
#
#  Class
#
# ////////////////////////////////////////////////////////////////////////// #
class MaximumNumberError(Exception):
    pass

class MinimummNumberError(Exception):
    pass

class SplitFileNotExist(Exception):
    pass

# ////////////////////////////////////////////////////////////////////////// #
#
#  Function
#
# ////////////////////////////////////////////////////////////////////////// #
def displayFileExistsError(filename):

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : FileExistsError")
    print("------------------------------------------------------------")
    print(" Message : There is a file with the same name.")
    print("")
    print("           Move {} and try again.".format(filename))
    print("============================================================")
    print("")

def displayMaximumNumberError():

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : MaximumNumberError")
    print("------------------------------------------------------------")
    print(" Message : The argument is large.")
    print("")
    print("           Check the number of files.")
    print("============================================================")
    print("")

def displayMinimummNumberError():

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : MinimummNumberError")
    print("------------------------------------------------------------")
    print(" Message : The argument is small.")
    print("")
    print("           Check the number of files.")
    print("============================================================")
    print("")

def displayFileNotFoundError(filename)

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : FileNotFoundError")
    print("------------------------------------------------------------")
    print(" Message : The specified file does not exist.")
    print("")
    print("           Can't find {}.".format(filename))
    print("============================================================")
    print("")

def displayValueError(number):

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : ValueError")
    print("------------------------------------------------------------")
    print(" Message : There is a file with the same name.")
    print("")
    print("           Move {} and try again.".format(number))
    print("============================================================")
    print("")

def displaySplitFileNotExist():

    print("")
    print("============================================================")
    print(" Warning!!")
    print("------------------------------------------------------------")
    print(" Type    : SplitFileNotExist")
    print("------------------------------------------------------------")
    print(" Message : The split file does not exist.")
    print("")
    print("           Make sure there are no missing pieces.")
    print("============================================================")
    print("")

def raiseMaximumNumberError():
    raise MaximumNumberError()

def raiseMinimummNumberError():
    raise MinimummNumberError()

def raiseSplitFileNotExist():
    raise SplitFileNotExist()


