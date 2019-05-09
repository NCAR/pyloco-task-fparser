# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import fparser.common.readfortran as readfortran
import fparser.two.parser as fortranparser

import pickle
import pyloco

class Node(object):

    def __init__(self, node, uppernode):

        self.name = node.__class__.__name__
        self.uppernode = uppernode
        self.subnodes = []
        self.types = []

        if hasattr(node, "items"):
            self.types.append("expr") 

            for item in node.items:
                self.subnodes.append(Node(item, self))

        elif hasattr(node, "content"):
            self.types.append("stmt") 

            for item in node.content:
                self.subnodes.append(Node(item, self))


class FparserTask(pyloco.Task):
    """a wrapper task for fparser Python Fortran parser package

'fparser' task wraps fparser Python Fortran parser package to work with other Pyloco tasks.
Especially, this task uses the second version of fparser, 'fparser2', of the package to
parse down to expression level.


Example
-------

Following example read 'my.f90' Fortran source file and displays Abstract Syntax Tree (AST)
of the file on screen.

An example Fortran source file of 'my.f90'. ::

        program test
            integer, parameter :: x = 1, y = 2
            print *, x, "+", y, "=", x+y
        end program

An example pyloco command to parse 'my.f90'. ::

        >>> pyloco fparser my.f90 -- print
        PROGRAM test
          INTEGER, PARAMETER :: x = 1, y = 2
          PRINT *, x, "+", y, "=", x + y
        END PROGRAM test
"""
    _name_ = "fparser"
    _version_ = "0.1.0"

    def __init__(self, parent):

        self.add_data_argument("data", help="File to parse")

        self.add_option_argument("-o", "--output", help="Save AST as Python pickle file")

        self.register_forward("data", help="Output Abstract Syntax Tree")

    def perform(self, targs):

        reader = readfortran.FortranFileReader(
                    targs.data, ignore_comments=False)

        parser = fortranparser.ParserFactory().create(std="f2008")

        tree = parser(reader)

        if targs.output:
            with open(targs.output, "wb") as f:
                synnode = Node(tree, None)
                pickle.dump(synnode, f)

        self.add_forward(data=tree)
