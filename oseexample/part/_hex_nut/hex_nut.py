from math import radians, sqrt

import Part
from FreeCAD import Matrix, Vector
from oseexample.part._hexagonal_prism import HexagonalPrism


class HexNut:

    @staticmethod
    def make(flat_to_flat_distance: float = 10.0,
             hole_diameter: float = 6.0,
             height: float = 4.0) -> Part.Solid:
        if hole_diameter >= flat_to_flat_distance:
            error_message_template = 'Hole diameter of "{}" must be less than flat-to-flat distance of "{}".'
            raise ValueError(error_message_template.format(
                hole_diameter, flat_to_flat_distance))
        hexagonal_prism = HexagonalPrism.make(flat_to_flat_distance, height)
        cylinder = Part.makeCylinder(hole_diameter / 2.0, height)
        return hexagonal_prism.cut(cylinder)
