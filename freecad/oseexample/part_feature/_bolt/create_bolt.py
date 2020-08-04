from FreeCAD import Placement, Vector

from oseexample.model import BoltModel


def create_bolt(document, name):
    """
    Creates a part feature object with the given name,
    and adds it to the document.
    """
    obj = document.addObject('Part::FeaturePython', name)
    BoltModel(obj)
    obj.ViewObject.Proxy = 0  # Mandatory unless ViewProvider is coded
    return obj
