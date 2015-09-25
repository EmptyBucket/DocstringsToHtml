import os.path
import ast
from .info import Info


class Module(Info):

    """builds the documentation for the module"""

    def __init__(self, node, path_python_file):
        nameModule = os.path.basename(path_python_file)
        args = None
        docModule = ast.get_docstring(node)
        super(Module, self).__init__("Module", nameModule, args, docModule)
