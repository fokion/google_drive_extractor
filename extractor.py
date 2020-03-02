import getopt
import os
import shutil
import re
import sys
from zipfile import ZipFile


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

    for f in files:
        print(f)
        with ZipFile(os.path.join(path, f), 'r') as zipObj:
            names = zipObj.namelist()
            for name in names:
                clean_name = re.sub('[^0-9a-zA-Z]+', '', name)
                print(clean_name)
                if (name.endswith(".jpg") or name.endswith(".mp4") or name.endswith(
                        ".jpeg")) and not clean_name.startswith("TakeoutGooglePhotosHangout"):

                    parts = name.split("/")

                    name_without_path = parts[len(parts) - 1]

                    if not os.path.isfile(os.path.join(destination_path, name_without_path)):
                        try:
                            zipObj.extract(name, os.path.join(destination_path))
                            extracted_location = os.path.join(destination_path, name)
                            print(extracted_location)
                            if os.path.isfile(extracted_location):
                                print("Exists... ")
                                shutil.move(extracted_location, os.path.join(destination_path, name_without_path))
                                if not os.path.isfile(os.path.join(destination_path, name_without_path)):
                                    print("Moved file is not there...")
                                    exit(1)
                        except:
                            print("Could not extract " + name)
                    else:
                        print("Skip " + name_without_path)

        print("------------------")


if __name__ == '__main__':
    main(sys.argv[1:])
