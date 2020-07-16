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


if __name__ == '__main__':
    unittest.main()
