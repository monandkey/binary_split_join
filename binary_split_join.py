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
import os.path
import hashlib
import glob

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

# ////////////////////////////////////////////////////////////////////////// #
#
#  Function
#
# ////////////////////////////////////////////////////////////////////////// #
# ========================================================================== #
# Function name  ：BinarySplit
# -------------------------------------------------------------------------- #
# Discription　  ：バイナリファイルを分割する
# Return value   ：N/A
# ========================================================================== #
def BinarySplit(file, size=1024*1024*9):
    l = os.path.getsize(file)
    numberOfdivisions = round((l + size - 1) / size)
    last = (size * numberOfdivisions) - l

    b = open(file, 'rb')
    for i in range(numberOfdivisions):
        read_size = last if i == numberOfdivisions -1 else size
        data = b.read(read_size)
        out = open(file + '.frac' + str(i), 'wb')
        out.write(data)
        out.close()
    b.close()

    # md5sumを計算
    with open(file, 'rb') as f:
        checksum = hashlib.md5(f.read()).hexdigest()

    print("")
    print("============================================================")
    print(" Thank you for your patience. The file has been split.")
    print("============================================================")
    print(" Original file        : {}".format(file))
    print("------------------------------------------------------------")
    print(" Number of divisions  : {}".format(numberOfdivisions))
    print("------------------------------------------------------------")
    print(" hash value [ MD5 ]     : {}".format(checksum))
    print("------------------------------------------------------------")
    print(" Split files")
    print("------------------------------------------------------------")

    for i in range(numberOfdivisions):
        print(" +++++ {}.frac{}".format(file, i))

    print("============================================================")
    print("")

# ========================================================================== #
# Function name  BinaryJoin
# -------------------------------------------------------------------------- #
# Discription　  ：コマンドラインからファイル名を取得する、"-h"フラグが存在する場合はプログラミング終了する
# Return value   ：N/A
# ========================================================================== #
def BinaryJoin(file, num):

    try:

        # フォルダ内に指定された数のファイルが存在するか確認
        DIR = '.'
        directorynum = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

        if (directorynum -1) < num:
            raise MaximumNumberError()

        elif (directorynum -1) > num:
            raise MinimummNumberError()
        
        # ファイル結合処理
        out = open(file + '.out', 'wb')
        for i in range(num):
            frac = open(file + '.frac' + str(i), 'rb')
            out.write(frac.read())
            frac.close()
        out.close()

        # リネーム
        os.rename(file + '.out', file)

        # md5sumを計算
        with open(file, 'rb') as f:
            checksum = hashlib.md5(f.read()).hexdigest()

        print("")
        print("============================================================")
        print(" Thank you for your patience. The file has been split.")
        print("============================================================")
        print(" Result file          : {}".format(file))
        print("------------------------------------------------------------")
        print(" Number of divisions  : {}".format(num))
        print("------------------------------------------------------------")
        print(" hash value [ MD5 ]     : {}".format(checksum))
        print("------------------------------------------------------------")
        print(" Merged files")
        print("------------------------------------------------------------")

        for i in range(num):
            print(" ----- {}.frac{}".format(file, i))
            os.remove(file + '.frac' + str(i))

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
# メインパート
# ============================================================================
if __name__=='__main__':

    try:
        args_value = sys.argv

        os.path.exists(args_value[1])

        if "-h" in args_value[1]:
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

        # Expected
        # python binary_dc.py [filename] [num]
        if len(args_value) > 2:

            # 分割されたファイルが存在するか確認。無ければエラー処理
            if (len(glob.glob(args_value[1] + '.frac*'))) < 1:
                raise SplitFileNotExist()

            # ファイルを結合する関数へ移動
            BinaryJoin(args_value[1], int(args_value[2]))

        # Expected
        # python binary_dc.py [filename]
        elif len(args_value) > 1:

            # ファイルを分割する関数へ移動
            BinarySplit(args_value[1])

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

# ============================================================================
# EOF
# ============================================================================