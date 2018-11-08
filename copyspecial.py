#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    path = os.path.abspath(dir)
    files_list = os.listdir(path)
    special_paths = []
    # instructions say in all the directories, but there is only one directory currently do you mean do the os.path.walk?, or do you mean in the directory i indicate??
    for file in files_list:
        if re.search(r'__(\w+)__', file):
            special_paths.append(os.path.abspath(file))
    return special_paths


def copy_paths(paths_to_copy, dest_dir):
    if dest_dir[0] != '/':
        dest_dir = '/' + dest_dir
    dest_dir = os.getcwd() + dest_dir
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
    for file in paths_to_copy:
        shutil.copy(file, dest_dir)


def zippy(paths, zippath):
    a = os.path.abspath(zippath)
    for file in paths:
        cmd = "zip -j " + zippath + " " + file
        (status, _) = commands.getstatusoutput(cmd)
        if not os.path.exists(os.path.dirname(a)):
            print("oh no!")
            print("zip error: no file at: " + zippath)
            print('failed command: ' + cmd)
            return
        if status != 0:
            print("oh no!")
            print("zip error: oh no - couldn't do it!")
            print('failed command: ' + cmd)
            return
        print(cmd)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--todir', help='copy files to given directory', action='store_true')
    parser.add_argument(
        '--tozip', help='zips files into folder', action='store_true')
    parser.add_argument('dir', help='directory assigned', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.todir:
        list_special_paths = get_special_paths(args.dir[1])
        copy_paths(list_special_paths, args.dir[0])

    elif args.tozip:
        list_special_paths = get_special_paths(args.dir[1])
        zippy(list_special_paths, args.dir[0])
    else:
        for path in get_special_paths(args.dir):
            print(path)
    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).
    # shutil.copy('./staw_hat_random_owl.jpg', 'path')
    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
