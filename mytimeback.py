#!/usr/bin/env python

import difflib, sys
from termcolor import cprint

def compare (a,b):
  if a != b:
    cprint ('ALERT: DIFFERENCE DETECTED', 'white', 'on_red')
    cprint ('Detailed diff below', 'red')
    for line in difflib.context_diff(a, b):
        sys.stdout.write(line)
  elif a == b:
    cprint ('NO DIFFERNCE FOUND', 'white', 'on_green')
  else:
    cprint ('BAD DATASETS')

if __name__ == '__main__':
  with open ("file1.txt", "r") as file1:
      dataset1=file1.readlines()

  with open ("file2.txt", "r") as file2:
      dataset2=file2.readlines()

  compare (dataset1, dataset2)

