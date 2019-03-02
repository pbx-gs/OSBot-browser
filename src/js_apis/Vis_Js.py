import json

from browser.Browser_Lamdba_Helper import Browser_Lamdba_Helper
from utils.Dev import Dev


class Vis_Js:
    def __init__(self):
        #self.base_html_file = '/vis-js/empty.html'
        self.base_html_file = '/vis-js/simple.html'
        #window.api_visjs
        self.browser        = None

    def add_edge__js_code(self, from_node, to_node):
        edge = {'from': str(from_node), 'to': str(to_node)}
        return 'network.body.data.edges.add({0});'.format(json.dumps(edge))

    def add_edge(self, from_node, to_node):
        self.exec_js(self.add_edge__js_code(from_node,to_node))
        return self

    def add_node__js_code(self, node_id, node_label, shape='box', color=None):
        node = {'id': str(node_id), 'label': str(node_label), 'shape': shape, 'color': color}
        return 'network.body.data.nodes.add({0});'.format(json.dumps(node))

    def add_node(self,node_id, node_label, shape='box',color=None):
        self.exec_js(self.add_node__js_code(node_id, node_label, shape, color))
        return self

    def exec_js(self,js_code):
        return self.browser.api_browser.sync__js_execute(js_code)

    def setup(self):
        self.browser = Browser_Lamdba_Helper().setup()
        #self.browser.open_local_file(, js_code)
        self.browser.open_local_file(self.base_html_file)
        return self


    #def create_screenshot(self):
    #    return self.browser().sync__screenshot()
