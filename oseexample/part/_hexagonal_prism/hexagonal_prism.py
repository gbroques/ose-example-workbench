from math import radians, sqrt

import Part
from FreeCAD import Matrix, Vector


class HexagonalPrism:

    @staticmethod
    def make(minimal_diameter: float = 10.0, height: float = 6.0) -> Part.Solid:
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
    :return: Hexagon wire
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
