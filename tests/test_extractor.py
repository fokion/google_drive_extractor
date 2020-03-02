import os
import unittest

from zip_extractor import ZipExtractor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        path = os.getcwd()
        extractor = ZipExtractor(path)
        extractor.extract_zip_to_destination(os.path.join(path,"takeout-202003022105-001.zip"))
        exported_file=os.path.join(path,"test.jpg")
        self.assertTrue(os.path.isfile(exported_file))
        os.remove(exported_file)



if __name__ == '__main__':
    unittest.main()
