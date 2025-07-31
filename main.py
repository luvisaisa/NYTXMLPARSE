"""Launch the NYTXML GUI application."""

from nyt_xmlparse import NYTXMLGuiApp
import tkinter as tk


def main() -> None:
    root = tk.Tk()
    NYTXMLGuiApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
