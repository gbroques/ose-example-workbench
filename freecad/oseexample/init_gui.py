"""Imported when FreeCAD starts up to add workbench to GUI."""
import FreeCAD as App
import FreeCADGui as Gui

from .icon import get_icon_path
from .OSE_Example import register_commands


class ExampleWorkbench(Gui.Workbench):
    """
    Example Workbench
    """
    MenuText = 'OSE Example'
    ToolTip = \
        'A workbench for designing Example machines by Open Source Ecology'
    Icon = get_icon_path('Box.svg')

    def Initialize(self):
        """
        Executed when FreeCAD starts
        """
        main_toolbar, main_menu = register_commands()

        self.appendToolbar('OSE Example', main_toolbar)
        self.appendMenu('OSE Example', main_menu)

    def Activated(self):
        """
        Executed when workbench is activated.
        """
        if not(App.ActiveDocument):
            App.newDocument()

    def Deactivated(self):
        """
        Executed when workbench is deactivated.
        """
        pass

    def GetClassName(self):
        return 'Gui::PythonWorkbench'


Gui.addWorkbench(ExampleWorkbench())
