#!/usr/bin/env python3
"Symlinks files, mostly configuration ones"
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='Named directory to traverse',
                    default='/traverse')
args = parser.parse_args()

directory = args.directory
if directory[-1] == '/':
    directory = directory[:-1]

for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        traverse_filename = dirpath + '/' + filename
        container_filename = dirpath[len(directory):] + '/' + filename
        try:
            os.remove(container_filename)
        except FileNotFoundError:
            pass  # OK
        os.symlink(traverse_filename, container_filename)
