import os
import unittest

from extensions_parser import ExtensionsParser


class ExtensionsParserTest(unittest.TestCase):
    def test_parse(self):
        extensions = set()
        extensions.update([".json", ".ai"])
        parsed_extensions = ExtensionsParser.parse(os.path.join(os.getcwd(), "extensions.conf"))
        print(parsed_extensions)
        self.assertSetEqual(extensions,parsed_extensions)


if __name__ == '__main__':
    unittest.main()
