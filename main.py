from docstrings_to_html import DocstringsToHTML, FileNotPy
import argparse
import sys
import os


def test():
        lever = DocstringsToHTML.test()
        if not lever:
            print("Test is passed")
        else:
            print("Test fails")


def normal():
    path_python_file = args.path_python_file
    path_html_dir = args.path_html_dir

    template = None
    if args.template:
        template = args.template

    layout = None
    if args.layout:
        layout = args.layout

    try:
        if args.directory:
            for root, dirs, files in os.walk(path_python_file):
                for name in files:
                    try:
                        if name[:-3] + ".html" in \
                                next(os.walk(path_html_dir))[2]:
                            continue
                    except Exception:
                        pass

                    python_path = os.path.join(root, name)
                    try:
                        docstrings_to_hTML = DocstringsToHTML(
                            python_path, path_python_file,
                            path_html_dir, template, layout)
                        docstrings_to_hTML.translate()
                    except FileNotPy:
                        continue
        else:
            python_dir = os.path.dirname(path_python_file)
            docstrings_to_hTML = DocstringsToHTML(
                path_python_file, python_dir, path_html_dir, template, layout)
            docstrings_to_hTML.translate()
    except Exception as e:
        sys.exit("Error: {0}".format(e))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="DocstringsToHtml",
        description="purpose docstringsToHtml - translation of "
        "documents from Python docstring to html",
        epilog="Copyright (C) 2015 Politov Alexey Version 1.0")
    sub_parsers = parser.add_subparsers(title="use normal or test mode")

    test_parser = sub_parsers.add_parser("test")
    test_parser.set_defaults(func=test)

    normal_parser = sub_parsers.add_parser("normal")
    normal_parser.add_argument(
        "path_python_file", help="python path to the file "
        "with the code and documentation in a format string to "
        "translate documents into HTML documents")
    normal_parser.add_argument(
        "path_html_dir", help="the path to the directory to output")
    normal_parser.add_argument(
        "-t", "--template", help="template for output",
        action="store", type=str)
    normal_parser.add_argument(
        "-l", "--layout", help="template layout for output",
        action="store", type=str)
    normal_parser.add_argument(
        "-d", "--directory", help="the path to the python file is "
        "now perceived as a directory", action="store_true")
    normal_parser.set_defaults(func=normal)

    args = parser.parse_args()
    try:
        args.func()
    except AttributeError:
        parser.parse_args(["-h"])
