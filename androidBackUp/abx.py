# coding=utf-8

import argparse
import os
import sys
import zlib

# Android Backup description: 
# http://nelenkov.blogspot.com.ar/2012/06/unpacking-android-backups.html

C_BUFFER_SIZE = 1048576


def ArgParse():
    """
    Parses the command line arguments
    :return: argparse dictionary
    """
    # parse command line arguments
    parser = argparse.ArgumentParser(
        description="xbackup: extracts an Android ICS+ backup file.")
    parser.add_argument("ipath",
                        help="Input path.")
    parser.add_argument("opath",
                        help="Input path.")
    args = parser.parse_args()
    return args


def Extract(args):
    """
    Extracts the .tar file of an Android Backup. Assumes the backup is not encrypted and is
    compressed.
    :param args:
    :return:
    """
    ifile = open(args.ipath, "rb")
    ofile = open(args.opath, "wb")
    data = ifile.read(C_BUFFER_SIZE)
    pos = data.find("none\n") + 5
    data = data[pos:]
    dc = zlib.decompressobj()
    while data:
        ofile.write(dc.decompress(data))
        data = ifile.read(C_BUFFER_SIZE)
    ifile.close()
    ofile.close()


def main():
    args = ArgParse()
    if os.path.isfile(args.ipath):
        Extract(args)
    else:
        print "Could not open input file!."
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
