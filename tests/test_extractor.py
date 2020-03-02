import os
import unittest

from zip_extractor import ZipExtractor


class ExtractorTest(unittest.TestCase):
    def test_extracting(self):
        path = os.getcwd()
        extractor = ZipExtractor(path,{})
        extractor.extract_zip_to_destination(os.path.join(path,"takeout-202003022105-001.zip"))
        exported_file=os.path.join(path,"test.jpg")
        self.assertTrue(os.path.isfile(exported_file))
        os.remove(exported_file)

    def test_extracting_extra_extension(self):
        path = os.getcwd()
        extractor = ZipExtractor(path, {".json"})
        extractor.extract_zip_to_destination(os.path.join(path, "takeout-202003022105-001.zip"))
        exported_file_image = os.path.join(path, "test.jpg")
        exported_file_json = os.path.join(path, "test.json")
        self.assertTrue(os.path.isfile(exported_file_image))
        self.assertTrue(os.path.isfile(exported_file_json))
        os.remove(exported_file_image)
        os.remove(exported_file_json)



if __name__ == '__main__':
    unittest.main()
