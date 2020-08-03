import FreeCAD as App
import Part

from freecad.oseexample.icon import get_icon_path
from freecad.oseexample.part_feature import create_hex_nut


class AddHexNutCommand:
    """
    Command to add a Hex Nut.
    """

    NAME = 'AddHexNut'

    def Activated(self):
        document = App.ActiveDocument
        if not document:
            document = App.newDocument()
        create_hex_nut(document, 'HexNut')
        document.recompute()

    def IsActive(self):
        return True

    def GetResources(self):
        return {
            'Pixmap': get_icon_path('HexNut.svg'),
            'MenuText': 'Add Hex Nut',
            'ToolTip': 'Add Hex Nut'
        }
