"""Command Registry Module"""
import FreeCADGui as Gui

from .command import AddHexNutCommand

#: Command Namespace
command_namespace = 'OSEExample'


def register_commands():
    """
    Register all workbench commands,
    and associate them to toolbars, menus, sub-menus, and context menu.
    """
    add_hex_nut_key = _register(AddHexNutCommand.NAME, AddHexNutCommand())

    #: Main Toolbar Commands
    main_toolbar_commands = [
        add_hex_nut_key
    ]

    return main_toolbar_commands


def _register(name, command):
    key = '{}_{}'.format(command_namespace, name)
    Gui.addCommand(key, command)
    return key
