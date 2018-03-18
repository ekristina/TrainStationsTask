import unittest

from definitions import TownNode, DistanceEdge, RouteGraph


class TestRouteDistance(unittest.TestCase):

    """Unittests to test distance calculations between nodes"""

    def setUp(self):
        """Creates TownNodes and Graphs for each test"""
        # creating Towns
        self.a = TownNode("A")
        self.b = TownNode("B")
        self.c = TownNode("C")
        self.d = TownNode("D")
        self.e = TownNode("E")

        # creating routes
        self.graph = {
            self.a: [DistanceEdge(self.a, self.b, 5),
                     DistanceEdge(self.a, self.d, 5),
                     DistanceEdge(self.a, self.e, 7)],
            self.b: [DistanceEdge(self.b, self.c, 4)],
            self.c: [DistanceEdge(self.c, self.d, 8),
                     DistanceEdge(self.c, self.e, 2)],
            self.d: [DistanceEdge(self.d, self.c, 8),
                     DistanceEdge(self.d, self.e, 6)],
            self.e: [DistanceEdge(self.e, self.b, 3)]
        }

    def test_distance_abc(self):
        """The distance of the route A-B-C."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_full_distance([self.a, self.b, self.c]),
            9
        )

    def test_distance_ad(self):
        """The distance of the route A-D."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_full_distance([self.a, self.d]),
            5
        )

    def test_distance_adc(self):
        """The distance of the route A-D-C."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_full_distance((self.a, self.d, self.c)),
            13
        )

    def test_distance_aebcd(self):
        """The distance of the route A-E-B-C-D."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_full_distance((self.a, self.e, self.b, self.c, self.d)),
            22
        )

    def test_distance_aed(self):
        """The distance of the route A-E-D."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_full_distance((self.a, self.e, self.d)),
            "NO SUCH ROUTE"
        )


class TestNumberOfTripsWithStops(unittest.TestCase):

    """Unittests for counting number of trips with
        given max or exact number of stops"""

    def setUp(self):
        """Creates TownNodes and Graphs for each test"""
        # creating Towns
        self.a = TownNode("A")
        self.b = TownNode("B")
        self.c = TownNode("C")
        self.d = TownNode("D")
        self.e = TownNode("E")

        # creating routes
        self.graph = {
            self.a: [DistanceEdge(self.a, self.b, 5),
                     DistanceEdge(self.a, self.d, 5),
                     DistanceEdge(self.a, self.e, 7)],
            self.b: [DistanceEdge(self.b, self.c, 4)],
            self.c: [DistanceEdge(self.c, self.d, 8),
                     DistanceEdge(self.c, self.e, 2)],
            self.d: [DistanceEdge(self.d, self.c, 8),
                     DistanceEdge(self.d, self.e, 6)],
            self.e: [DistanceEdge(self.e, self.b, 3)]
        }

    def test_number_of_trips_c_to_c(self):
        """The number of trips starting at C and ending at C with a maximum of 3
            stops.  In the sample data below, there are two such trips: C-D-C (2
            stops). and C-E-B-C (3 stops)."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_possible_routes_max_stops(self.c, self.c,
                                                                          max_stops=3),
            2
        )

    def test_number_of_trips_a_to_c_exact(self):
        """The number of trips starting at A and ending at C with exactly 4 stops.
            In the sample data below, there are three such trips: A to C (via B,C,D); A
            to C (via D,C,D); and A to C (via D,E,B)."""
        self.assertEqual(
            RouteGraph(routes=self.graph).count_possible_routes_fixed_stops(self.a, self.c,
                                                                            fixed_stops=4),
            3
        )


if __name__ == '__main__':
    unittest.main()
