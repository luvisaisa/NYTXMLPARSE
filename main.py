"""Example script using NYTXMLParser."""

from nyt_xmlparse import NYTXMLParser

if __name__ == "__main__":
    parser = NYTXMLParser()
    sample_xml = "<root><item>NYT</item></root>"
    root = parser.parse(sample_xml)
    print(root.tag)
