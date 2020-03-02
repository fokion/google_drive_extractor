import getopt
import os
import shutil
import re
import sys
from zipfile import ZipFile

from zip_extractor import ZipExtractor


def main(argv):
    path = ''
    destination_path = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('extractor.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('extractor.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            path = arg
        elif opt in ("-o", "--ofile"):
            destination_path = arg

    if not(path!="" and destination_path!="" and os.path.isdir(path) and os.path.isdir(destination_path)):
        print('Not specified paths or not folders')
        print('Try running extractor.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    print('Input folder is "', path)
    print('Output folder is "', destination_path)
    files = []

    for filename in os.listdir(path):
        if filename.endswith(".zip") and filename.startswith("takeout-"):
            files.append(filename)

    extractor = ZipExtractor(destination_path)
    for f in files:
        extractor.extract_zip_to_destination(os.path.join(path, f))




if __name__ == '__main__':
    main(sys.argv[1:])
