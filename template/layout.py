import sys
import os
import pystache


class Layout(object):

    """docstring for Layout"""

    def __init__(self, path_layout, header, data):
        super(Layout, self).__init__()
        if path_layout is None:
            path_layout = os.path.join(
                sys.path[0], "template", "default_layout.html")
        with open(path_layout, "r") as layout:
            layout = layout.read()

        renderer = pystache.Renderer()
        self.html = renderer.render(
            layout, {"header": header, "data": data})

    def get_html(self):
        return self.html
