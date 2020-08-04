import FreeCAD as App

from freecad.oseexample.icon import get_icon_path
import Part


class AddBoltCommand:
    """Command to add bolt."""

    NAME = 'AddBolt'

    def Activated(self):
        document = App.ActiveDocument
        if not document:
            document = App.newDocument()
        Part.show(Part.makeBox(10, 10, 10))
        # document.recompute()

    def IsActive(self):
        return True

    def GetResources(self):
        return {
            'Pixmap': get_icon_path('Bolt.svg'),
            'MenuText': 'Add Bolt',
            'ToolTip': 'Add Bolt'
        }
