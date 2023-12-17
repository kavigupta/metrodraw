import unittest

from metrodraw.model.coord import Coord
from metrodraw.model.railmap import Railmap
from tests.utils import produce_or_check_images


class SimpleSingleLineTest(unittest.TestCase):
    def test_single_line(self):
        origin = Coord(0, 0)

        rm = Railmap()

        line = rm.line(origin, "orange", "Line")
        line.station("South")
        line.station("Middle", "ur")
        line.station("North", "ur")

        rm.propagate_positioning()

        produce_or_check_images(rm, "simple_single_line")
