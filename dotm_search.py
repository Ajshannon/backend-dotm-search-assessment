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
import argparse



def run(text, path):
    files_searched = 0
    matches = 0
    os.chdir(path)
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
    print "Files matched: " + str(matches)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', help='choose text to seach for')
    parser.add_argument('--dir', help='add a directory, default is cwd')
    args = parser.parse_args()

    text = args.text
    directory = args.dir
    if directory:
        run(text, directory)
    else: 
        run(text, )
    

if __name__ == "__main__":
    main()