#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-14
Purpose: Expand IUPAC codes
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Expand IUPAC codes',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='SEQ',
                        nargs='+',
                        help='Input sequence(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    iupac_table = {'A': 'A',
                   'C': 'C',
                   'G': 'G',
                   'T': 'T',
                   'U': 'U',
                   'R': '[AG]',
                   'Y': '[CT]',
                   'S': '[GC]',
                   'W': '[AT]',
                   'K': '[GT]',
                   'M': '[AC]',
                   'B': '[CGT]',
                   'D': '[AGT]',
                   'H': '[ACT]',
                   'V': '[ACG]',
                   'N': '[ACGT]'}

    # print(iupac_table)
    for seq in args.seq:
        print(seq, end='', file=args.outfile)
        print(' ', end='', file=args.outfile)
        for base in seq:
            if base in iupac_table:
                print(iupac_table[base], end='', file=args.outfile)
        print(file=args.outfile)

    if args.outfile != sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
