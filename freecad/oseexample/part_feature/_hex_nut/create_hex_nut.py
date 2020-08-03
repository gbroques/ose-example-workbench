from FreeCAD import Placement, Vector

from oseexample.model import HexNutModel


def create_hex_nut(document, name):
    """
    Creates a part feature object with the given name,
    and adds it to the document.
    """
    obj = document.addObject('Part::FeaturePython', name)
    HexNutModel(obj)
    obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
    return obj
