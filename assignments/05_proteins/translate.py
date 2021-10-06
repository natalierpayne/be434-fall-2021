#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-05
Purpose: translate nucleic acid to amino acid
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='translate nucleic acid to amino acid',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('nucacid',
                        metavar='str',
                        help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        required=True,
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(args.nucacid)


# --------------------------------------------------
if __name__ == '__main__':
    main()
