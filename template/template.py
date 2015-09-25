import sys
import os
import pystache


class Template(object):

    """docstring for Template"""

    def __init__(self, path_template, header, doc, offset=0):
        super(Template, self).__init__()
        if path_template is None:
            path_template = os.path.join(
                sys.path[0], "template", "default_template.html")
        with open(path_template, "r") as template:
            template = template.read()

        renderer = pystache.Renderer()
        self.html = renderer.render(
            template, {"offset": offset, "header": header, "doc": doc})

    def get_html(self):
        return self.html
