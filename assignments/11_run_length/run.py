#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-11-14
Purpose: Run-length encoding/data compression
"""

import argparse
import os

# pylint: disable=undefined-loop-variable
# pylint: disable=consider-using-with
# pylint: disable=unspecified-encoding


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()
    if os.path.isfile(args.str):
        args.str = open(args.str).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.str.splitlines():
        print(rle(seq), end='')


# --------------------------------------------------
def rle(seq):
    """ Create RLE """

    base_count = 0
    for num, base in enumerate(seq):
        if num == 0:
            base_count = 1
        else:
            if base == seq[num - 1]:
                base_count += 1
            else:
                if base_count == 1:
                    print(seq[num - 1], end='')
                    base_count = 1
                    # ^ reminder that for current base, also 1
                else:
                    print(f'{seq[num - 1]}{base_count}', end='')
                    base_count = 1
    if base_count == 1:
        print(base)
    else:
        print(f'{base}{base_count}')

    # ^ makes sure very last base also gets printed

    return ''


# --------------------------------------------------
# def test_rle():
#     """ Test rle """

#     assert rle('A') == 'A'
#     assert rle('ACGT') == 'ACGT'
#     assert rle('AA') == 'A2'
#     assert rle('AAAAA') == 'A5'
#     assert rle('ACCGGGTTTT') == 'AC2G3T4'
# doesn't work with return ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
