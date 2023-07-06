"""
Model for rolling horizon used in dispatch.
"""

from andes.core import (ModelData, NumParam)  # NOQA

from ams.core.model import Model  # NOQA


class Horizon(ModelData, Model):
    """
    Rolling horizon.
    """

    def __init__(self, system=None, config=None):
        ModelData.__init__(self)
        Model.__init__(self, system, config)
        self.group = 'TimeHorizon'

        self.nt = NumParam(default=6,
                           info='number of intervals',
                           tex_name=r'n_{t}',
                           )
        self.dt = NumParam(default=60,
                           info='time interval in minutes',
                           tex_name='\delta_{t}',
                           unit='min',
                           )
