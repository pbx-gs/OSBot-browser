from unittest import TestCase

from Go_Js_Views import Go_Js_Views
from browser.Browser_Lamdba_Helper import Browser_Lamdba_Helper
from utils.Dev import Dev
from utils.aws.Lambdas import Lambdas
from view_helpers.View_Examples import View_Examples


class Test_Go_Js_Views(TestCase):

    def setUp(self):
        self.graph_name = 'graph_XKW'
        self.png_data   = None

    def tearDown(self):
        if self.png_data:
            Browser_Lamdba_Helper(headless=False).save_png_data(self.png_data)

    def test_default(self):
        graph_name = 'graph_XKW'    # (7 nodes)
        graph_name = 'graph_MKF'    # ( 20 nodes,  27 edges)
        #graph_name = 'graph_YT4'   # (199 nodes, 236 edges)
        #graph_name = 'graph_VZ5'   # (367 nodes, 653 edges)
        #graph_name = 'graph_EE3'    # fails in lambda in visjs (but works here :) )

        self.png_data = Go_Js_Views.default(params=[graph_name])

    def test_circular (self): self.png_data = Go_Js_Views.circular (params=['graph_MKF'])
    def test_sankey   (self): self.png_data = Go_Js_Views.sankey   (params=['graph_MKF'])
    def test_swimlanes(self): self.png_data = Go_Js_Views.swimlanes(params=['graph_MKF'])
    def test_mindmap  (self): self.png_data = Go_Js_Views.mindmap  (params=['graph_IGF'])



    def test_open_file_in_browser__go_gs(self):
        #View_Examples(headless=False).open_file_in_browser('/go-js/sankey.html')
        View_Examples(headless=False).open_file_in_browser('/go-js/mindmap.html')

    def test_update_lambda(self):
        Lambdas('browser.lambda_browser').update_with_src()


    def test_invoke_via_lambda(self):
        Lambdas('browser.lambda_browser').update_with_src()

        payload = { "params" : ["go_js","graph_MKF", "default"]}
        self.png_data = Lambdas('browser.lambda_browser').invoke(payload)
        Dev.pprint(self.png_data)

        self.png_data = Lambdas('browser.lambda_browser').invoke(payload)
        Dev.pprint(self.png_data)