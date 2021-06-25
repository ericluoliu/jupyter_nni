# -*- coding: utf-8 -*-

# import method from handlers.py called load_jupyter_server_extension
from .handlers import load_jupyter_server_extension   # noqa


__version__ = "0.2.0"

#standard method required for all jupyter NOTEBOOK EXTENSIONS
def _jupyter_nbextension_paths():
    name = __name__ #__name__ is set to the name of the file being run, often it will just be __main__
    section = "main" #in the jupyter notebook the extension is called tree.js
    src = "static"
    return [dict(
        section=section,
        src=src, #path is relative to the __name__ directory
        dest=name, #directory in the nbextension namespace
        require="%s/%s" % (name, section))] #simply denotes that both name and section are strings --> "name/section" --> "__main__/tree" --> tree.js is entry point
        #https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting


#standard method required for all jupyter SERVER EXTENSIONS
def _jupyter_server_extension_paths():
    return [{
        "module": __name__
    }]
