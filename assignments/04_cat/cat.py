#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-09-28
Purpose: Python cat
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile',
                        metavar='FILE', 
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)') #type? needed to fail w/o file. but makes input file unreadable?

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    #infile = str(args.infile)

    #print(args.infile)

    if os.path.isfile(args.infile):
        infile = open(args.infile).read().rstrip()
    else:
        print("[Errno 2] No such file or directory: " + os.path.basename(args.infile))

    #for fh in args.infile:

    #print(infile)


# --------------------------------------------------
if __name__ == '__main__':
    main()
