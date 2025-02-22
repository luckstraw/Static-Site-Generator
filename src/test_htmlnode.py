import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        node = HTMLNode(tag='a', props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_no_props(self):
        node = HTMLNode(tag='p')
        self.assertEqual(node.props_to_html(), '')

    def test_repr(self):
        node = HTMLNode(tag='p', value='Hello', children=[], props={"class": "text"})
        expected_repr = "HTMLNode(tag=p, value=Hello, children=[], props={'class': 'text'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
