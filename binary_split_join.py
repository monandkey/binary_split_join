#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

# ////////////////////////////////////////////////////////////////////////// #
#
#   Module import
#
# ////////////////////////////////////////////////////////////////////////// #
# -------------------------------------------------------------------------- #
#  Default module
# -------------------------------------------------------------------------- #
import sys
import os
import hashlib
import glob

from module import app
from module import split
from module import join

# ////////////////////////////////////////////////////////////////////////// #
#
#  Class
#
# ////////////////////////////////////////////////////////////////////////// #
# 自作エラー
class MaximumNumberError(Exception):
    pass

class MinimummNumberError(Exception):
    pass

class SplitFileNotExist(Exception):
    pass

# ============================================================================
# メインパート
# ============================================================================
if __name__=='__main__':

    try:
        appinstance = app.setup()
        appinstance.processBranching()
        args_value = appinstance.getArgs()

        # Expected
        # python binary_dc.py [filename] [num]
        if len(args_value) > 2:

            # 分割されたファイルが存在するか確認。無ければエラー処理
            if (len(glob.glob(args_value[1] + '.div*'))) < 1:
                raise SplitFileNotExist()

            joininstance = join.setup(args_value[1], int(args_value[2]))
            joininstance.joinBinary()
            joininstance.displayResult()

        elif len(args_value) > 1:

            splitinstance = split.setup(args_value[1])
            splitinstance.splitBinary()
            splitinstance.displayResult()

    # 対象ファイルが存在しない場合
    except FileNotFoundError:

        print("")
        print("============================================================")
        print(" Warning!!")
        print("------------------------------------------------------------")
        print(" Type    : FileNotFoundError")
        print("------------------------------------------------------------")
        print(" Message : The specified file does not exist.")
        print("")
        print("           Can't find {}.".format(args_value[1]))
        print("============================================================")
        print("")

    # 引数が整数以外の場合
    except ValueError:

        print("")
        print("============================================================")
        print(" Warning!!")
        print("------------------------------------------------------------")
        print(" Type    : ValueError")
        print("------------------------------------------------------------")
        print(" Message : There is a file with the same name.")
        print("")
        print("           Move {} and try again.".format(args_value[2]))
        print("============================================================")
        print("")

    # 分割されたファイルが存在しない場合
    except SplitFileNotExist:

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

    # 同名のファイルが存在する場合
    except FileExistsError:

        print("")
        print("============================================================")
        print(" Warning!!")
        print("------------------------------------------------------------")
        print(" Type    : FileExistsError")
        print("------------------------------------------------------------")
        print(" Message : There is a file with the same name.")
        print("")
        print("           Move {} and try again.".format(file))
        print("============================================================")
        print("")

    # 引数の指定が分割されたファイルより大きい場合
    except MaximumNumberError:

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

    # 引数の指定が分割されたファイルより少ない場合
    except MinimummNumberError:

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

# ============================================================================
# EOF
# ============================================================================