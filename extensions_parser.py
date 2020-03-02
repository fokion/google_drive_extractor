import os


class ExtensionsParser:
    @staticmethod
    def parse(extensions_file):
        extensions = set()
        if os.path.isfile(extensions_file):
            with open(extensions_file) as f:
                list_extensions = f.read().splitlines()
                for item in list_extensions:
                    extension = "." + item
                    if item.startswith("."):
                        extension = item
                    extensions.add(extension.lower())
        return extensions
