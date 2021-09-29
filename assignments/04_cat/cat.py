#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-09-28
Purpose: Python cat
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Python cat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('infile',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # line_num = 0
    if args.number:
        for fh in args.infile:
            for num, line in enumerate(fh, start=1):
                num_string = "{:>6}".format(str(num))
                print(num_string + "\t" + line, end='')
                # print('     ' + str(num) + "\t" + line, end='')
                # ^ only good if single digit no. of lines!
                # line_num += 1
    else:
        for fh in args.infile:
            for line in fh:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
