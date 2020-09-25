Project Name: 
Auto Test

Author: 
  Justin Lee Lipper

Project Description:
  This program takes into account your operating system (limited to Windows and Linux as of 24092020) and runs your python assignment with test cases.

Versioning:
  Using: Python 3.8.2

Requirements:
  This program assumes that your assignment is labeled using the following convention "assignmentX-X.py". For example, "assignement3-1.py", "assignment1-1.py"...etc.
  This program assumes that the test_X-X-X.in files are all in the same directory as your assignment file.
  This program will only work with Windows and Linux

Execution:
  There are four different options for this script:
    1). "-c" Takes no arguments, and assumes that the directory to your assignment and test files, is the current directory
        $ python3 autoTest.py -c
    2). "-s" Takes one argument that is the directory to your assignment and test files.
        $ python3 autoTest.py -s /mnt/c/Users/$USER/...etc
    3). "-o" Works like -c but will also output the test_X-X-X.in files after each result.
        $ python3 autoTest.py -o
    4). Running the script with no flags will get you a default prompt that asks you for a directory string.
        $ python3 autoTest.py
    5). If you need a reminder or any additional help, then run the following:
        $ python autoTest.py -h
