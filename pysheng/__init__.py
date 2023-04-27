#!/usr/bin/env python3
import sys
__version__ = "0.3.0"
def console():
    from pysheng.download import main
    sys.exit(main(sys.argv[1:]))


def main_gui(args):
    import pysheng.gui as pysheng_gui
    import gi
    try:
    	gi.require_version('Gtk', '4.0')
    except:
    	gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk

    pysheng_gui.main(args)

   # book_url = (args[0] if args else None)
   # widgets, state = pysheng_gui.run(book_url)
   # app = Gtk.Application()
   # app.connect('activate', lambda _: widgets.window.present())
   # print(widgets)
   # print("===============================")
   # app.run()
#    widgets.window.show_all()
    #Gtk.main()

def gui():
    sys.exit(main_gui(sys.argv[1:]))
