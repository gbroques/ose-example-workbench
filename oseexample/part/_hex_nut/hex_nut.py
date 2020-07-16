from math import radians, sqrt

import Part
from FreeCAD import Matrix, Vector


class HexNut:

    @staticmethod
    def make():
        height = 4
        hexagonal_prism = make_hexagonal_prism(10, height)
        cylinder = Part.makeCylinder(3, height)
        return hexagonal_prism.cut(cylinder)


def make_hexagonal_prism(minimal_diameter: float, height: float) -> Part.Solid:
    hexagon_wire = make_hexagon_wire(minimal_diameter)
    hexagon_face = Part.Face(hexagon_wire)
    return hexagon_face.extrude(Vector(0, 0, height))


def make_hexagon_wire(minimal_diameter: float) -> Part.Wire:
    """Make hexagon wire.
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
