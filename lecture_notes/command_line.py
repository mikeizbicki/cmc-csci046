#! /usr/bin/python3

import sys

#sys.argv
# list containing all command
# line parameters

#print('sys.argv=',sys.argv)

# the glob = *
# replaces the glob with all files that match the specified pattern

# if you use argparse,
# do not use sys.argv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_file',
    help='the file we are going to process'
    )
parser.add_argument(
    '--num_lines',
    type=int,
    help='number of lines to process'
    )
args = parser.parse_args()

print('input_file=',args.input_file)
#print('num_lines=',args.num_lines+1)

# working with zip files
import zipfile

with zipfile.ZipFile(args.input_file) as f:
    print('files=',f.namelist())

    with f.open(f.namelist()[0]) as f2:
        num_tweets = 0
        for line in f2:
            num_tweets += 1
            #print('line=',line)
            #break

        print('num_tweets=',num_tweets)

# new programming technique is MapReduce
# invented by Google in 2004
# makes things efficient, parallel
# makes robust to errors in your code
# an example of divide and conquer algorithms

# in order to use MapReduce, create two files
# map.py file that processes an individual zip
# the map.py files don't depend each other
# reduce.py file that merges processing steps

from collections import deque, defaultdict, Counter


