import ast
from .__module import Module
from .__class import Class
from .__function import Function
from .__import import Import, ImportFrom


class PyDocModule(object):

    """structured pulls out all the documentation"""

    def __init__(
            self, path_python_file, python_dir, used_import, not_exist_import):
        super(PyDocModule, self).__init__()
        self.path_python_file = path_python_file
        self.python_dir = python_dir

        with open(path_python_file, encoding='utf-8') as python_file:
            python_code = python_file.read()
            module = ast.parse(python_code)

        self.paths_imports = []

        self.list_node = []
        self.list_node.append(Module(module, path_python_file))
        self.list_node.append(
            self.get_node_module_doc(module, used_import, not_exist_import))

    def get_list_node(self):
        """returns a list of nodes"""
        return self.list_node

    def get_node_module_doc(self, node, used_import, not_exist_import):
        """returns structured documentation"""
        list_node = []
        for node_child in ast.iter_child_nodes(node):
            if type(node_child) in (
                    ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom):

                if type(node_child) is ast.FunctionDef:
                    obj = Function(node_child)

                elif type(node_child) is ast.ClassDef:
                    obj = Class(node_child)

                elif type(node_child) in (ast.Import, ast.ImportFrom):
                    if type(node_child) is ast.Import:
                        obj = Import(node_child)
                    elif type(node_child) is ast.ImportFrom:
                        obj = ImportFrom(node_child)

                    self.paths_imports.extend(obj.create_doc_imports(
                        self.python_dir, used_import, not_exist_import))

                list_node.append(obj)
                list_node.append(
                    self.get_node_module_doc(
                        node_child, used_import, not_exist_import))
        return list_node

    def get_paths_imports(self):
        return self.paths_imports
