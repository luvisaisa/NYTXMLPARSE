# NYTXMLPARSE

Sample utilities to parse NYT-style XML files.

```
from nyt_xmlparse import NYTXMLParser

parser = NYTXMLParser()
root = parser.parse("<root></root>")
print(root.tag)
```
