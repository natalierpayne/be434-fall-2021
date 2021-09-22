#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-09-20
Purpose: Solfege
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='solfege',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('solfege',
                        metavar='str', nargs='+',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    solfege_defs = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'
    }

    for word in args.solfege:
        if word in solfege_defs:
            print(word + ', ' + solfege_defs[word])
        else:
            print("I don't know " + '"' + word + '"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
