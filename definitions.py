__author__ = "ekristina"


class TownNode:
    """Nodes represent towns"""
    def __init__(self, name: str):
        self.name = name
        self.visited = False

    def __repr__(self):
        # to print out a proper representation
        return self.name

    def __str__(self):
        # in case you need to make str(TownNode)
        return self.name

    def __hash__(self):
        # the TownNode type has to be hashable
        # Exists for the equality purposes
        # when the TownNode is used in dicts as a key
        return hash(self.name)

    # def __eq__(self, other):
    #     # check for equality
    #     return (self.__class__ == other.__class__ and
    #             self.name == other.name)


class DistanceEdge:
    """Edges represent distances between towns"""
    def __init__(self,
                 parent_node: TownNode,
                 destination: TownNode,
                 weight: int):

        self.parent_node = parent_node
        self.distance = weight
        self.destination = destination

    def __repr__(self):
        # to print out a proper representation
        return f"{self.parent_node.name}{self.destination.name}{self.distance}"

    def __str__(self):
        # in case you need to make str(DistanceEdge)
        return f"{self.parent_node.name}{self.destination.name}{self.distance}"


class RouteGraph:

    def __init__(self, towns: tuple or list, routes: dict):
        self.towns = towns
        self.routes = routes

    def count_full_distance(self):
        """

        Count full distance between all the given Nodes
        :return: int distance or str "NO SUCH ROUTE"
        """
        res = 0
        if len(self.towns) == 0:
            return res


        def __shift_list(lst):
            return lst[1:]

        # make tuples of two so [A,B,C] becomes [(A,B), (B,C)]
        paths = zip(self.towns, __shift_list(self.towns))
        for path in list(paths):
            distances = self.routes[path[0]]

            for dist in distances:
                if dist.destination == path[1]:
                    res += dist.distance
                    break

            else:
                return "NO SUCH ROUTE"

        return res

    def count_possible_routes(self, start: TownNode, finish: TownNode, max_stops):
        """
        Counts number of possible trips between given Nodes
        :param start: first town to start route
        :param finish: last town to finish route
        :param max_stops: int of maximum possible routes
        :return: int or "NO SUCH ROUTE"
        """
        print()






