#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-10-29
Purpose: Split interleaved/paired reads
"""

import argparse
from Bio import SeqIO
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_files',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.input_files:
        basename = ''
        root = ''
        reader = SeqIO.parse(fh, 'fasta')
        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)
        # print(root, ext)
        for num, rec in enumerate(reader, start=1):
            # print(num, rec)
            if not os.path.isdir(args.outdir):
                os.mkdir(args.outdir)
            if num % 2 != 0:
                filename = ''.join(args.outdir + '/' + root + '_1' + ext)
                open(filename, 'a').write('>'+rec.id+'\n')
                open(filename, 'a').write(str(rec.seq)+'\n')
            if num % 2 == 0:
                filename = ''.join(args.outdir + '/' + root + '_2' + ext)
                open(filename, 'a').write('>'+rec.id+'\n')
                open(filename, 'a').write(str(rec.seq)+'\n')

    print(f'Done, see output in "{args.outdir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
