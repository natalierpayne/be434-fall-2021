#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-11-04
Purpose: Find conserved bases
"""

import argparse
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved bases',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    positions = defaultdict(list)

    for seq in args.file:
        for num, char in enumerate(seq.rstrip(), start=1):
            positions[num].append(char)
        print(seq, end='')

    for position in positions.values():
        pos_set = set(position)
        if len(pos_set) > 1:
            print('X', end='')
        else:
            print('|', end='')

    print()


# --------------------------------------------------
if __name__ == '__main__':
    main()
