#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Wordlist generator made easy for cracking"""

# TODO:
#input:
##  seperator

#output
##   WiFi
##   1337
##   email (domain)

import sys


def get_parser():
    """Get parser object for script wordgen.py."""
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("wordlist",
                        type=FileType('r'),
                        default=sys.stdin,
                        metavar="wordlist",
                        help="wordlist to scramble")
    parser.add_argument("-o", "--output",
                        action="store",
                        type=FileType('w'),
                        default=sys.stdout,
                        dest="outputfile",
                        metavar="file",
                        help="write output to file")
    parser.add_argument("-s", "--seperator",
                        metavar="seperator",
                        help="the seperator symbol of words on each line [! ? , .]")
    parser.add_argument("-l", "--leet",
                        metavar="leet",
                        default=False,
                        help="create l33tsp34k words")

    return parser


def initialize(args):
    wordlist = list()
    for line in args.wordlist:
        line = line.strip("\r").strip("\n")
        wordlist.append(line.lower())
        wordlist.append(line.capitalize())
    set(wordlist)
    return wordlist


def create_wordlist(words):
    numbers = [x for x in range(101)]
    numbers += [123, 12345, 666, 789, 890, 2017, 2018, 2019]
    output = list()

    def add_special_characters():
        for char in ["!", "?", "."]:
            output.append(word + char)

    def add_numbers():
        for number in numbers:
            output.append(word + str(number))

    for word in words:
        add_special_characters()
        add_numbers()

    print("Wordlist: {}".format(output))


if __name__ == "__main__":
    args = get_parser().parse_args()
    wordlist = initialize(args)

    if args.wifi:
        pass
    if args.leet:
        pass
    if args.email:
        try:
            pass
        except IOError:
            print("Parameter -d domain name is required!")

    create_wordlist(wordlist)
