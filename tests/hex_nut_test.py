import unittest

# Need to import FreeCAD
import FreeCAD as App  # noqa: F401

from oseexample.part import HexNut


class HexNutTest(unittest.TestCase):
    """
    Test for HexNut Part class.
    """

    def test_make(self):
        box = HexNut.make()
        self.assertEqual(box.TypeId, 'Part::TopoShape')


if __name__ == '__main__':
    unittest.main()
