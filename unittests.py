import unittest

from definitions import TownNode, DistanceEdge, RouteGraph


class TestRouteDistance(unittest.TestCase):
    # creating Towns
    a = TownNode("A")
    b = TownNode("B")
    c = TownNode("C")
    d = TownNode("D")
    e = TownNode("E")

    # creating routes
    graph = {
        a: [DistanceEdge(a, b, 5), DistanceEdge(a, d, 5),
            DistanceEdge(a, e, 7)],
        b: [DistanceEdge(b, c, 4)],
        c: [DistanceEdge(c, d, 8), DistanceEdge(c, e, 2)],
        d: [DistanceEdge(d, c, 8), DistanceEdge(d, e, 6)],
        e: [DistanceEdge(e, b, 3)]
    }

    """Unittests to test distance calculations between nodes"""

    def test_distance_abc(self):
        self.assertEqual(
            RouteGraph(towns=[self.a, self.b, self.c],
                       routes=self.graph).count_full_distance(),
            9
        )

    def test_distance_ad(self):
        self.assertEqual(
            RouteGraph(towns=[self.a, self.d],
                       routes=self.graph).count_full_distance(),
            5
        )

    def test_distance_adc(self):
        self.assertEqual(
            RouteGraph(towns=(self.a, self.d, self.c),
                       routes=self.graph).count_full_distance(),
            13
        )

    def test_distance_aebcd(self):
        self.assertEqual(
            RouteGraph(towns=(self.a, self.e, self.b, self.c, self.d),
                       routes=self.graph).count_full_distance(),
            22
        )

    def test_distance_aed(self):
        self.assertEqual(
            RouteGraph(towns=(self.a, self.e, self.d),
                       routes=self.graph).count_full_distance(),
            "NO SUCH ROUTE"
        )

if __name__ == '__main__':
    unittest.main()

#
# pos_routes_CC3 = RouteGraph((a,b,c,d,e), routes=graph).count_possible_routes(c, c, 3)
# print(pos_routes_CC3)