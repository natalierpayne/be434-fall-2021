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
    
    words_file1 = []
    words_file2 = []
    kmers_file1 = {}
    kmers_file2 = {}

    for line in args.file1:
        line_split = line.rstrip().split()
        for word in line_split:
            words_file1.append(word)
            for kmer in find_kmers(word, args.kmer):
                kmer_count = 0
                for word in words_file1:
                    if kmer in word:
                        kmer_count += word.count(kmer)
                kmers_file1[kmer] = kmer_count
    # print(kmers_file1)

    word = ''

    for line in args.file2:
        line_split2 = line.rstrip().split()
        for word in line_split2:
            words_file2.append(word)
            for kmer in find_kmers(word, args.kmer):
                kmer_count = 0
                for word in words_file2:
                    if kmer in word:
                        kmer_count += word.count(kmer)
                kmers_file2[kmer] = kmer_count
                # kmers_file2[kmer] = words_file2.count(kmer) #won't work if kmer not whole word
    # print(kmers_file2)

    word = ''
    matches = []

    for kmer in kmers_file2:
        if kmer in kmers_file1:
            print(f'{kmer:10} {kmers_file1.get(kmer):5} {kmers_file2.get(kmer):5}')
            # matches.append(word)
    # unique_matches = list(set(matches))

    # for match in unique_matches:
    #     print(match, words_file1.count(match), words_file2.count(match))


# --------------------------------------------------
if __name__ == '__main__':
    main()
