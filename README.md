# NYTXMLPARSE

Sample utilities to parse NYT-style XML files.

```
from nyt_xmlparse import NYTXMLParser

parser = NYTXMLParser()
root = parser.parse("<root></root>")
print(root.tag)
```

To launch the graphical interface that can parse multiple XML files and export
the results to Excel, run:

```
from nyt_xmlparse import NYTXMLGuiApp
import tkinter as tk

root = tk.Tk()
NYTXMLGuiApp(root)
root.mainloop()
```

The export feature relies on ``openpyxl``. Install it via ``pip install openpyxl``.
