import Part

from oseexample.part._hexagonal_prism import HexagonalPrism


class Bolt:

    @staticmethod
    def make() -> Part.Shape:
        minimal_diameter = 10.0
        height = 6.0
        shaft = Part.makeCylinder(3, 35)
        hexagonal_prism = HexagonalPrism.make(minimal_diameter, height)
        return shaft.fuse(hexagonal_prism).removeSplitter()
