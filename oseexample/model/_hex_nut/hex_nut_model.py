import Part
from osecore.app.model import Model
from oseexample.part import HexNut


class HexNutModel(Model):

    Type = 'OSEHexNut'

    def __init__(self, obj):
        super(HexNutModel, self).__init__(obj)
        # TODO: Add custom properties
        # obj.addProperty('App::PropertyLength', 'PropertyName',
        #         'Base', 'Descriptive tooltip').PropertyName = 10.0

    def execute(self, obj):
        """
        Called on document recompute
        """
        obj.Shape = HexNut.make()

    def __getstate__(self):
        return self.Type

    def __setstate__(self, state):
        if state:
            self.Type = state
