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
                        nargs = '+',
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
    
    iupac_table = {'A':'A', 
                   'C':'C', 
                   'G':'G', 
                   'T':'T', 
                   'U':'U', 
                   'R':'[AG]', 
                   'Y':'[CT]', 
                   'S':'[GC]', 
                   'W':'[AT]', 
                   'K':'[GT]', 
                   'M':'[AC]', 
                   'B':'[CGT]', 
                   'D':'[AGT]', 
                   'H':'[ACT]', 
                   'V':'[ACG]', 
                   'N':'[ACGT]'}

    # print(iupac_table)
    for base in args.seq:
        print(base, end='')
    print(' ', end='')
    for base in args.seq:
        print(base)
        # if base in iupac_table:
        #     print(iupac_table.get(base)) # :(


# --------------------------------------------------
if __name__ == '__main__':
    main()
