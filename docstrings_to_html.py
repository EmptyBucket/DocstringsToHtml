import os
from sys import path
from py_doc.py_doc_module import PyDocModule
from template.template import Template
from template.layout import Layout


used_import = []
not_exist_import = []


class FileNotPy(Exception):

    """file not type html exception"""

    pass


class DocstringsToHTML(object):

    """documentation of the python interpreter dokstring in html"""

    def __init__(
            self, path_python_file, python_dir, html_dir, template, layout):
        super(DocstringsToHTML, self).__init__()
        self.template = template
        self.layout = layout
        self.python_dir = python_dir
        self._path_python_file = path_python_file
        if self._path_python_file[-3:] != ".py":
            raise FileNotPy("File is not py format")
        if not os.path.exists(html_dir):
            os.makedirs(html_dir)

        self.html_dir = html_dir
        html_name = os.path.basename(path_python_file)[:-3] + ".html"
        self._path_html_file = os.path.join(html_dir, html_name)

        self._doc_module = PyDocModule(
            path_python_file, python_dir, used_import, not_exist_import)
        paths_imports = self._doc_module.get_paths_imports()
        for path_import in paths_imports:
            docstrings_to_HTML = DocstringsToHTML(
                path_import, self.python_dir,
                self.html_dir, self.template, self.layout)
            docstrings_to_HTML.translate()

    def translate(self):
        """translation of documents from python dokstring in html"""
        list_node = self._doc_module.get_list_node()
        format_str_info = self._get_format_str_info(list_node)

        layout = Layout(self.layout, self._path_python_file, format_str_info)

        with open(self._path_html_file, 'w') as html_file:
            html_file.write(layout.get_html())

    def _get_format_str_info(self, list_node, offset=-4):
        """returns the formatted information and "
        "creates files for hyperlinks"""
        str_info = ""
        offset += 4
        for i in range(0, len(list_node), 2):
            node = list_node[i]
            child_node = list_node[i + 1]

            template = Template(
                self.template, node.get_header(), node.get_doc(), offset)
            info = (template.get_html())

            str_info += info + "\n"
            str_info += self._get_format_str_info(child_node, offset)
        return str_info

    @staticmethod
    def test():
        """testing method"""
        lever = False

        path_py1 = os.path.join(path[0], "test", "test1.py")
        path_py1_dir = os.path.join(path[0], "test")
        path_Html1 = os.path.join(path[0], "test", "html1")
        docstrings_to_HTML = DocstringsToHTML(
            path_py1, path_py1_dir, path_Html1, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html1", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check1.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful documentation. "
                    "Python client file")
            else:
                print("Validation fails documentation. Python client file")
                lever = True

        path_py2 = os.path.join(path[0], "test", "test2.py")
        path_py2_dir = os.path.join(path[0], "test")
        path_Html2 = os.path.join(path[0], "test", "html2")
        docstrings_to_HTML = DocstringsToHTML(
            path_py2, path_py2_dir, path_Html2, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html2", "test2.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check2.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful documentation. "
                    "Python server file")
            else:
                print("Validation fails documentation. Python server file")
                lever = True

        path_py3 = os.path.join(path[0], "test", "test1.py")
        path_py3_dir = os.path.join(path[0], "test")
        path_Html3 = os.path.join(path[0], "test", "html3")
        docstrings_to_HTML = DocstringsToHTML(
            path_py3, path_py3_dir, path_Html3, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html3", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check3_func.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful construct function")
            else:
                print("Validation fails construct function")
                lever = True

        path_py4 = os.path.join(path[0], "test", "test1.py")
        path_py4_dir = os.path.join(path[0], "test")
        path_Html4 = os.path.join(path[0], "test", "html4")
        docstrings_to_HTML = DocstringsToHTML(
            path_py4, path_py4_dir, path_Html4, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html4", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check4_class.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful construct class")
            else:
                print("Validation fails construct class")
                lever = True

        path_py5 = os.path.join(path[0], "test", "test1.py")
        path_py5_dir = os.path.join(path[0], "test")
        path_Html5 = os.path.join(path[0], "test", "html5")
        docstrings_to_HTML = DocstringsToHTML(
            path_py5, path_py5_dir, path_Html5, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html5", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check5_import.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful construct import")
            else:
                print("Validation fails construct import")
                lever = True

        path_py6 = os.path.join(path[0], "test", "test1.py")
        path_py6_dir = os.path.join(path[0], "test")
        path_Html6 = os.path.join(path[0], "test", "html6")
        docstrings_to_HTML = DocstringsToHTML(
            path_py6, path_py6_dir, path_Html6, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html6", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test",
                    "check6_from_import.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful construct from import")
            else:
                print("Validation fails construct from import")
                lever = True

        path_py7 = os.path.join(path[0], "test", "test1.py")
        path_py7_dir = os.path.join(path[0], "test")
        path_Html7 = os.path.join(path[0], "test", "html7")
        docstrings_to_HTML = DocstringsToHTML(
            path_py7, path_py7_dir, path_Html7, None, None)
        docstrings_to_HTML.translate()

        with open(os.path.join(path[0], "test", "html7", "test1.html"), "r") as doc,\
                open(os.path.join(
                    path[0], "test", "check7_link.html"), "r") as check:
            if check.read() in doc.read():
                print(
                    "Verification was successful construct link")
            else:
                print("Validation fails construct link")
                lever = True

        print("Complete test")

        return lever
