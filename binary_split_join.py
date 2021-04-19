#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

import sys
import os
import hashlib
import glob

from module import app
from module import split
from module import join
from module import error

if __name__=='__main__':

    try:
        appinstance = app.setup()
        appinstance.processBranching()
        args_value = appinstance.getArgs()

        if len(args_value) > 2:

            if (len(glob.glob(args_value[1] + '.div*'))) < 1:
                error.raiseSplitFileNotExist()

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

    except error.SplitFileNotExist:
        error.displaySplitFileNotExist()

    except FileExistsError:
        error.displayFileExistsError(args_value[1])
