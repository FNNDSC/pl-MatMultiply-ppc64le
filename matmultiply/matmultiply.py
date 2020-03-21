#!/usr/bin/env python                                            #
# matmultiply ds ChRIS plugin app
#
# (c) 2016-2019 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import sys
import MatCal

sys.path.append(os.path.dirname(__file__))

# import the Chris app superclass
from chrisapp.base import ChrisApp

Gstr_title = """
███╗   ███╗ █████╗ ████████╗███╗   ███╗██╗   ██╗██╗  ████████╗██╗██████╗ ██╗  ██╗   ██╗
████╗ ████║██╔══██╗╚══██╔══╝████╗ ████║██║   ██║██║  ╚══██╔══╝██║██╔══██╗██║  ╚██╗ ██╔╝
██╔████╔██║███████║   ██║   ██╔████╔██║██║   ██║██║     ██║   ██║██████╔╝██║   ╚████╔╝ 
██║╚██╔╝██║██╔══██║   ██║   ██║╚██╔╝██║██║   ██║██║     ██║   ██║██╔═══╝ ██║    ╚██╔╝  
██║ ╚═╝ ██║██║  ██║   ██║   ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║██║     ███████╗██║   
╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚══════╝╚═╝   
                                                                                       


"""

Gstr_synopsis = """
(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)
    NAME
       matmultiply.py 
    SYNOPSIS
        python matmultiply.py                                         \\
            <inputDir>                                                  \\
            <outputDir> 
    BRIEF EXAMPLE
        * Bare bones execution
            mkdir in out && chmod 777 out
            python matmultiply.py   \\
                                in    out
    DESCRIPTION
        `matmultiply.py` ...
    ARGS

"""


class Matmultiply(ChrisApp):
    """
    An app to ....
    """
    AUTHORS = 'kefan (kefan29@bu.edu)'
    SELFPATH = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC = os.path.basename(__file__)
    EXECSHELL = 'python3'
    TITLE = 'A ChRIS plugin app'
    CATEGORY = ''
    TYPE = 'ds'
    DESCRIPTION = 'An app to ...'
    DOCUMENTATION = 'http://wiki'
    VERSION = '0.1'
    ICON = ''  # url of an icon image
    LICENSE = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        obj = MatCal.MatMulBench()
        print(obj.Run())

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)


# ENTRYPOINT
if __name__ == "__main__":
    chris_app = Matmultiply()
    chris_app.launch()
