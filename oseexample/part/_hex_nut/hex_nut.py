from math import radians, sqrt

import Part
from FreeCAD import Matrix, Vector


class HexNut:

    @staticmethod
    def make(flat_to_flat_distance: float = 10.0,
             hole_diameter: float = 6.0,
             height: float = 4.0) -> Part.Solid:
        if hole_diameter >= flat_to_flat_distance:
            error_message_template = 'Hole diameter of "{}" must be less than flat-to-flat distance of "{}".'
            raise ValueError(error_message_template.format(
                hole_diameter, flat_to_flat_distance))
        hexagonal_prism = make_hexagonal_prism(flat_to_flat_distance, height)
        cylinder = Part.makeCylinder(hole_diameter / 2.0, height)
        return hexagonal_prism.cut(cylinder)


def make_hexagonal_prism(minimal_diameter: float, height: float) -> Part.Solid:
    hexagon_wire = make_hexagon_wire(minimal_diameter)
    hexagon_face = Part.Face(hexagon_wire)
    return hexagon_face.extrude(Vector(0, 0, height))


def make_hexagon_wire(minimal_diameter: float) -> Part.Wire:
    r"""Make hexagon wire.
    ::
          _____     ┯
         /     \    |
        /       \   | minimal diameter
        \       /   |
         \_____/    |
                    ┷
    :param minimal_diameter: Diameter of the inscribed circle
                             distance between parallel sides,
                             or flat-to-flat distance.
    :type minimal_diameter: float
    :return: Hexagon wire
    :rtype: Part.Wire
    """
    matrix = Matrix()
    matrix.rotateZ(radians(60))
    hexagon_vertices = []
    vector = Vector(minimal_diameter / sqrt(3), 0, 0)
    for i in range(6):
        hexagon_vertices.append(vector)
        vector = matrix.multiply(vector)
        hexagon_vertices.append(vector)
    return Part.makePolygon(hexagon_vertices)
