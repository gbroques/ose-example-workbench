import Part
from osecore.app.model import Model
from oseexample.part import Bolt


class BoltModel(Model):

    Type = 'OSEBolt'

    def __init__(self, obj):
        super(BoltModel, self).__init__(obj)
        obj.addProperty('App::PropertyLength', 'WidthAcrossFlats',
                        'Base', 'Flat-to-flat distance.').WidthAcrossFlats = 10.0
        obj.addProperty('App::PropertyLength', 'HeadHeight',
                        'Base', 'Height of bolt head.').HeadHeight = 6.0
        obj.addProperty('App::PropertyLength', 'ShaftRadius',
                        'Base', 'Radius of shaft.').ShaftRadius = 3.0
        obj.addProperty('App::PropertyLength', 'ShaftHeight',
                        'Base', 'Height of shaft.').ShaftHeight = 35.0

    def execute(self, obj):
        """
        Called on document recompute
        """
        flat_to_flat_distance = obj.WidthAcrossFlats.Value
        head_height = obj.HeadHeight.Value
        shaft_radius = obj.ShaftRadius.Value
        shaft_height = obj.ShaftHeight.Value
        obj.Shape = Bolt.make(flat_to_flat_distance,
                              head_height, shaft_radius, shaft_height)

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
