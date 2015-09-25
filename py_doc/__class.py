from .info import Info
import ast


class Class(Info):

    """builds the documentation for the class"""

    def __init__(self, node):
        name = node.name
        bases = []
        for base in node.bases:
            try:
                bases.append(base.id)
            except AttributeError:
                try:
                    bases.append(base.value.id + "." + base.attr)
                except AttributeError:
                    pass
        doc = ast.get_docstring(node)
        super(Class, self).__init__("Class", name, bases, doc)
