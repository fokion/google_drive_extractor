import os
import re
import shutil
from zipfile import ZipFile


class ZipExtractor:
    def __init__(self, destination_path):
        self.destination_path = destination_path

    def extract_zip_to_destination(self,file):
        with ZipFile(file, 'r') as zipObj:
            names = zipObj.namelist()
            for name in names:
                clean_name = re.sub('[^0-9a-zA-Z]+', '', name)
                print(clean_name)
                if (name.endswith(".jpg") or name.endswith(".mp4") or name.endswith(
                        ".jpeg")) and not clean_name.startswith("TakeoutGooglePhotosHangout"):

                    parts = name.split("/")

                    name_without_path = parts[len(parts) - 1]

                    if not os.path.isfile(os.path.join(self.destination_path, name_without_path)):
                        try:
                            zipObj.extract(name, os.path.join(self.destination_path))
                            extracted_location = os.path.join(self.destination_path, name)
                            print(extracted_location)
                            if os.path.isfile(extracted_location):
                                shutil.move(extracted_location, os.path.join(self.destination_path, name_without_path))
                                if not os.path.isfile(os.path.join(self.destination_path, name_without_path)):
                                    print("Moved file is not there...")
                                    exit(1)
                        except:
                            print("Could not extract " + name)
                    else:
                        print("Skip " + name_without_path)
        print("------------------")
