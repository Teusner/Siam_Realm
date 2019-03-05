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


class Animal:
    def __init__(self, x, y, dir, map):
        self.__coords = x,y
        self.__direction = dir

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, ncoords):
        nx,ny=ncoords
        if nx < 5 and ny < 5 :
            self.__coords = nx,ny

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, ndir):
        if ndir % 90 == 0:
            self.__direction = ndir

    def move(self, nx, ny):
        self.coords = (nx,ny)

    def rotate(self, dir):
        self.direction = dir


class Elephant(Animal):
    def __init__(self, x, y, dir, map):
        super().__init__(x, y, dir, map)
        self._car = 'E'

    def __str__(self):
        return 'Elephant : [Position = (' + str(self.coords[0]) + \
               ',' + str(self.coords[1]) + ') ; Direction = '+ \
               str(self.direction) + ']\n'


class Rhinoceros(Animal):
    def __init__(self, x, y, dir, map):
        super().__init__(x, y, dir, map)
        self.car = 'R'

    def __str__(self):
        return 'Rhinoceros : [Position = (' + str(self.coords[0]) + \
               ',' + str(self.coords[1]) + ') ; Direction = '+ \
               str(self.direction) + ']\n'


if __name__ == '__main__':
    a = Elephant(0, 2, 90, 10)
    b = Rhinoceros(0, 2, 90, 10)
    b.move(1,5)
    a.rotate(180)
    print(a, b)