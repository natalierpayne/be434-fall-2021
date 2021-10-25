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

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    def find_kmers(seq, k):
        """ Find k-mers in string """

        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i:i + k] for i in range(n)]

    # def test_find_kmers():
    #     """ Test find_kmers """

    #     assert find_kmers('', 1) == []
    #     assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    #     assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    #     assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    #     assert find_kmers('ACTG', 4) == ['ACTG']
    #     assert find_kmers('ACTG', 5) == []

    kmers_file1 = {}
    kmers_file2 = {}

    for line in args.file1:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer not in kmers_file1:
                    kmers_file1[kmer] = 0
                kmers_file1[kmer] += 1

    word = ''

    for line in args.file2:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer not in kmers_file2:
                    kmers_file2[kmer] = 0
                kmers_file2[kmer] += 1

    word = ''

    for kmer in sorted(kmers_file2):
        if kmer in kmers_file1:
            print(f'{kmer:10}',
                  f'{kmers_file1.get(kmer):5}',
                  f'{kmers_file2.get(kmer):5}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
