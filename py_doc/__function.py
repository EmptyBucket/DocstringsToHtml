from .info import Info
import ast
import _ast


class Function(Info):

    """builds the documentation for the function"""

    def __init__(self, node):
        name = node.name
        args = []
        if node.args.args is not None:
            for argument in node.args.args:
                args.append(argument.arg)
            for default, num_arg in zip(
                    reversed(node.args.defaults), reversed(range(len(args)))):
                if type(default) is _ast.Str:
                    args[num_arg] += ' = "' + default.s + '"'
                elif type(default) is _ast.NameConstant:
                    args[num_arg] += " = " + str(default.value)
                elif type(default) is _ast.Num:
                    args[num_arg] += " = " + str(default.n)
                elif type(default) is _ast.Name:
                    args[num_arg] += " = " + str(default.id)

        if node.args.vararg is not None:
            args.append("*" + node.args.vararg.arg)

        if node.args.kwarg is not None:
            args.append("**" + node.args.kwarg.arg)

        doc = ast.get_docstring(node)
        super(Function, self).__init__("Function", name, args, doc)
