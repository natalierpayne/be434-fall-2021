#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-07
Purpose: Find common words
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')

    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')                    

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words_file1 = []
    words_file2 = []

    for line in args.file1:
        line_split = line.rstrip().split()
        for word in line_split:
            words_file1.append(word)
    # print(words_file1)

    word = ''

    for line in args.file2:
        line_split2 = line.rstrip().split()
        for word in line_split2:
            words_file2.append(word)
    # print(words_file2)

    word = ''
    matches = []

    for word in words_file2:
        if word in words_file1:
            # print(word)
            matches.append(word)
    matches = sorted(matches)
    match_str = '\n'.join([str(x)for x in matches])
    print(match_str, file=args.outfile)
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
