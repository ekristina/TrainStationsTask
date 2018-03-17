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
        # to be able to be a key of a dictionary
        return hash(self.name)

    def __eq__(self, other):
        # check for equality, also used when TownNode is a key of a dictionary
        # otherwise KeyError will be raised
        return (self.__class__ == other.__class__ and
                self.name == other.name)


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
    """
    RouteGraph is a class which initially takes
    the full graph with all the nodes
    and all the edges in the following format:

    graph = {TownNode1: [DistanceEdge1, DistanceEdge2...],
             TownNode2: [DistanceEdge3, DistanceEdge4]}
    """

    def __init__(self, routes: dict):
        self.routes = routes  # full graph (all nodes, all edges)

    def count_full_distance(self, towns):
        """
        Count full distance between all the given Nodes

        :param towns: list or tuple of TownNodes to perform calculations with
        :return: int distance or str "NO SUCH ROUTE"
        """
        res = 0
        if len(towns) == 0:
            return res

        def __shift_list(lst):
            return lst[1:]

        # make tuples of two so [A,B,C] becomes [(A,B), (B,C)]
        paths = zip(towns, __shift_list(towns))
        for path in paths:
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






