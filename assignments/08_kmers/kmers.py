#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-20
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        type=argparse.FileType('rt'),
                        help='Input file 1')
    
    parser.add_argument('file2',
                        metavar='FILE2',
                        type=argparse.FileType('rt'),
                        help='Input file 2')

    parser.add_argument('-k',
                        '--kmer',
                        help='kmer size',
                        metavar='int',
                        type=int,
                        default=3)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args)


# --------------------------------------------------
if __name__ == '__main__':
    main()
