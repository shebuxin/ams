"""
Base class for variables.
"""

from typing import Optional

import numpy as np


class Algeb:
    """
    Algebraic variable class.

    This class is revised from ``andes.core.var.Algeb``.
    """

    def __init__(self,
                 name: Optional[str] = None,
                 tex_name: Optional[str] = None,
                 info: Optional[str] = None,
                 unit: Optional[str] = None,
                 ):
        self.name = name
        self.info = info
        self.unit = unit

        self.tex_name = tex_name if tex_name else name
        self.owner = None  # instance of the owner Model
        self.id = None     # variable internal index inside a model (assigned in run time)
        self.v = np.empty(0)  # variable value

    def __repr__(self):
        n = self.owner.n
        dev_text = 'Algeb' if n == 1 else 'Algebs'
        return f'{self.owner.__class__.__name__}.{self.name} ({n} {dev_text}) at {hex(id(self))}'


class RAlgeb:
    """
    Class for algebraic variable in a routine.

    This class is an extension of ``Algeb`` that revise the tex name and 
    """
    def __init__(self,
                 Algeb: Algeb,
                 ):
        self.Algeb = Algeb
        self.name = Algeb.name
        self.info = Algeb.info
        self.unit = Algeb.unit

        tex_name = Algeb.tex_name
        mname = Algeb.owner.__class__.__name__
        self.tex_name = f'{Algeb.tex_name}_' + '{' + f'{mname}' + '}' if tex_name else self.name
        self.owner = Algeb.owner  # instance of the owner Model
        self.v = np.empty(0)  # variable value

