import unittest

# Need to import FreeCAD
import FreeCAD as App  # noqa: F401

from oseexample.part import HexNut


class HexNutTest(unittest.TestCase):
    """
    Test for HexNut Part class.
    """

    def test_make(self):
        hex_nut = HexNut.make()
        self.assertEqual(len(hex_nut.Faces), 9)
        self.assertEqual(hex_nut.TypeId, 'Part::TopoShape')

    def test_make_when_hole_diameter_is_greater_than_or_equal_to_flats_distance_raises_value_error(self):
        flat_to_flat_distance = 10
        hole_diameter = 10
        with self.assertRaises(ValueError):
            HexNut.make(flat_to_flat_distance, hole_diameter)


if __name__ == '__main__':
    unittest.main()
