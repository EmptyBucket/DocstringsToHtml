from .info import Info
from abc import ABCMeta
import os


class ParentImport(object):

    """docstring for ParentImport"""
    __metaclass__ = ABCMeta

    @staticmethod
    def find_import_directory(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def create_doc_imports(
            self, python_dir,
            used_import, not_exist_import):
        paths_imports = []
        links = []
        for imp in self.imports:
            import_name = imp.split(".").pop()
            if import_name in not_exist_import:
                continue

            path_html = import_name + ".html"

            link = ("<a href='{0}'>{1}</a>").format(path_html, import_name)

            if import_name in used_import:
                links.append(link)
                continue
            else:
                path_import = ParentImport.find_import_directory(
                    import_name + ".py", python_dir)
                if path_import is None:
                    not_exist_import.append(import_name)
                    continue
                else:
                    used_import.append(import_name)
                    links.append(link)
                    paths_imports.append(path_import)
        if links == []:
            self.set_doc("Not local import, use the help()")
        else:
            self.set_doc(', '.join(links))
        return paths_imports


class Import(ParentImport, Info):

    """builds the documentation for the import"""

    def __init__(self, node):
        self.path_import = []
        names = []
        for name in node.names:
            names.append(name.name)

        self.imports = names

        header = ", ".join(names)
        super(Import, self).__init__("Import", header, None, None)


class ImportFrom(ParentImport, Info):

    """builds the documentation for the from import"""

    def __init__(self, node):
        self.path_import = []
        names = []
        for name in node.names:
            names.append(name.name)

        self.imports = [node.module]

        header = "from " + node.module + " import " + ", ".join(names)
        super(ImportFrom, self).__init__("Import", header, None, None)
