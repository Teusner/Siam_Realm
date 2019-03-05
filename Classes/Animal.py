#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
'''

class Animal :
    def __init__(self, x, y, dir):
        self._coords = x,y
        self._direction = dir

    @property
    def coords (self):
        return self._coords

    @coords.setter
    def coords(self, nx,ny):
        if (nx<5 and ny<5) :
            self._coords = nx,ny

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, ndir):
        if (ndir%90==0):
            self._direction = ndir

    def move(self, nx, ny):
        if (nx < 5 and ny < 5):
            self._coords = nx,ny
            return True
        else:
            return None

    def rotate(self, dir):
        self._direction = dir

    def __str__(self):
        return 'Animal : [Position = (' + str(self._coords[0]) + ',' + str(self._coords[1]) + ') ; Direction = '+ str(self._direction) + ']\n'


if __name__=='__main__' :
    a=Animal(0,2,90)
    z=a.move(0,1)
    print(z)
    print('\n',a)