#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-05
Purpose: translate nucleic acid to amino acid
"""

import argparse
from pprint import pprint
import os


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
    # print('seq =', args.nucacid)
    # print('codons =', args.codons)
    # print('outfile =', args.outfile)
    codon_table={}
    codon_aa_pair=[]
    for line in args.codons:
        # print(line.rstrip().split())
        codon_aa_pair.append(line.rstrip().split())
    # print(codon_aa_pair) # a list of tuples
    for key, val in codon_aa_pair:
        codon_table[key] = val
    # pprint(codon_table) # print table for checking

    k = 3
    seq = args.nucacid
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        # print(codon.upper() + " " + codon_table.get(codon.upper(), '-'), file=args.outfile)
        print(codon_table.get(codon.upper(), '-'), file=args.outfile, end='')
    print('Output written to "' + args.outfile.name + '".') #issue here


# --------------------------------------------------
if __name__ == '__main__':
    main()
