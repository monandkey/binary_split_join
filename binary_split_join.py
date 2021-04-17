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

    except FileNotFoundError:
        error.displayFileNotFoundError(args_value[1])

    except ValueError:
        error.displayValueError(args_value[2])

    except SplitFileNotExist:
        error.displaySplitFileNotExist()

    except FileExistsError:
        error.displayFileExistsError(args_value[1])

    except MaximumNumberError:
        error.displayMaximumNumberError()

    except MinimummNumberError:
        error.displayMinimummNumberError()

# ============================================================================
# EOF
# ============================================================================