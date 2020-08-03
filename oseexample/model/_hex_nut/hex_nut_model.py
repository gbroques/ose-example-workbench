import Part
from osecore.app.model import Model
from oseexample.part import HexNut


class HexNutModel(Model):

    Type = 'OSEHexNut'

    def __init__(self, obj):
        super(HexNutModel, self).__init__(obj)
        
        obj.addProperty('App::PropertyLength', 'WidthAcrossFlats',
                'Base', 'Flat-to-flat distance.').WidthAcrossFlats = 10.0
        obj.addProperty('App::PropertyLength', 'HoleDiameter',
                'Base', 'Diameter of hole.').HoleDiameter = 6.0
        obj.addProperty('App::PropertyLength', 'Height',
                'Base', 'Height of hex-nut.').Height = 4.0

    def execute(self, obj):
        """
        Called on document recompute
        """
        flat_to_flat_distance = obj.WidthAcrossFlats.Value
        hole_diameter = obj.HoleDiameter.Value
        height = obj.Height.Value
        obj.Shape = HexNut.make(flat_to_flat_distance,
                                hole_diameter,
                                height)

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
