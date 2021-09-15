#!/usr/bin/env python3
"""
Author : nataliermercer <nataliermercer@localhost>
Date   : 2021-09-14
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('integers',
                        metavar='INT', type = int, nargs = '+',
                        help='numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    integers = args.integers
    
    if len(integers) == 1:
        one_int = integers[0]
        print(str(one_int) + ' = ' + str(one_int))
    else:
        int_str = [str(x) for x in integers]
        print(' + '.join(int_str) + ' = ' + str(sum(integers)))

 
# --------------------------------------------------
if __name__ == '__main__':
    main()
