#!/usr/bin/env python
"""
Given a directory path, this searches all files in the path for a given text string 
within the 'word/document.xml' section of a MSWord .dotm file.
"""

# Your awesome code begins here!

import os
import sys
import glob
import zipfile

cwd = os.getcwd() + '/dotm_files'

def run(text, path=cwd):
    files_searched = 0
    matches = 0
    os.chdir('./dotm_files')
    files = glob.glob('*.dotm')
    for filename in files:
        files_searched += 1
        zipf = zipfile.ZipFile(filename, 'r')
        texts = zipf.read('word/document.xml')
        if text in texts:
            output_text = ''
            index = texts.index(text)
            matches += 1
            output_text = 'Match found in file ' + filename + '\n' + '\t' + texts[index - 40: index + 40]
            print output_text
    print "files searched: " + str(files_searched)
    print "\n Files matched: " + str(matches)

run("$", cwd)
# if __name__ == "__main__"
#     with open("./input2.txt", "r") as f:
#         lines = f.read().split("\n")
#         for line in lines:
#             print nested_brackets(line)

# if __name__ == "__main__":
#     main()