from nyt_xmlparse import NYTXMLParser


def test_import():
    parser = NYTXMLParser()
    xml = "<root></root>"
    assert parser.parse(xml).tag == "root"
