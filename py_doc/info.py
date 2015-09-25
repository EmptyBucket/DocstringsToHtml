class Info(object):

    """creator of the information object"""

    def __init__(self, typeObj, name, args, doc):
        super(Info, self).__init__()
        self._type_obj = typeObj
        self._name = name
        self._args = args
        self._doc = doc

    def get_type(self):
        """returns the typeObj of"""
        return self._type_obj

    def get_name(self):
        """returns the name of"""
        return self._name

    def get_args(self):
        """returns the argument"""
        return self._args

    def get_doc(self):
        """returns documents"""
        if self._doc:
            return self._doc
        else:
            return "No documentation"

    def set_doc(self, doc):
        self._doc = doc

    def get_header(self):
        """returns the title"""
        if self._args:
            return self._type_obj + ": " + self._name + \
                "(" + ', '.join(self._args) + ")"
        elif self._args == []:
            return self._type_obj + ": " + self._name + \
                "( )"
        else:
            return self._type_obj + ": " + self._name
