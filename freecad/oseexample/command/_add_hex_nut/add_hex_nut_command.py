import FreeCAD as App
import Part

from freecad.oseexample.icon import get_icon_path
from oseexample.part import HexNut


class AddHexNutCommand:
    """
    Command to add a Hex Nut.
    """

    NAME = 'AddHexNut'

    def Activated(self):
        document = App.ActiveDocument
        if not document:
            document = App.newDocument()
        hex_nut = HexNut.make()
        Part.show(hex_nut)

    def IsActive(self):
        return True

    def GetResources(self):
        return {
            'Pixmap': get_icon_path('HexNut.svg'),
            'MenuText': 'Add Hex Nut',
            'ToolTip': 'Add Hex Nut'
        }
