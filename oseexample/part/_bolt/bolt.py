import Part

from oseexample.part._hexagonal_prism import HexagonalPrism


class Bolt:

    @staticmethod
    def make(flat_to_flat_distance: float = 10.0,
             head_height: float = 6.0,
             shaft_radius: float = 3.0,
             shaft_height: float = 35.0) -> Part.Solid:
        bolt_head = HexagonalPrism.make(flat_to_flat_distance, head_height)
        shaft = Part.makeCylinder(shaft_radius, shaft_height)
        return bolt_head.fuse(shaft).removeSplitter()
