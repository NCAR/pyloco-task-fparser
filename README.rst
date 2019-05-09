============================
'fparser' task version 0.1.0
============================

'fparser' task wraps fparser Python Fortran parser package to work with other Pyloco tasks.
Especially, this task uses the second version of fparser, 'fparser2', of the package to
parse down to expression level.

Installation
------------

Before installing 'fparser' task, please make sure that 'pyloco' is installed.
Run the following command if you need to install 'pyloco'. ::

    >>> pip install pyloco

Or, if 'pyloco' is already installed, upgrade 'pyloco' with the following command ::

    >>> pip install -U pyloco

To install 'fparser' task, run the following 'pyloco' command.  ::

    >>> pyloco install fparser

Command-line syntax
-------------------

usage: pyloco fparser [-h] [-o OUTPUT] [--general-arguments] data 

a wrapper task for fparser Python Fortran parser package

positional arguments:
  data                  File to parse

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Save AST as Python pickle file
  --general-arguments   Task-common arguments. Use --verbose to see a list of
                        general arguments

forward output variables:
   data                 Output Abstract Syntax Tree


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
