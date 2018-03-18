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
            # extract all the edges (distances) connecting
            # the Node to other nodes
            distances = self.routes[path[0]]

            for dist in distances:
                if dist.destination == path[1]:
                    res += dist.distance
                    break

            else:
                return "NO SUCH ROUTE"

        return res

    def count_trips_max_stops(self, start: TownNode,
                              finish: TownNode,
                              max_stops: int, stops: int = 0):
        """
        Counts number of possible trips between given Nodes
        :param stops: number of trips, default value
        :param start: first town to start route
        :param finish: last town to finish route
        :param max_stops: int of maximum possible stops
        :return: int of trips or "NO SUCH ROUTE"
        """
        if start not in self.routes or finish not in self.routes:
            # can be returned only immediately and not as a result of recursion
            return "NO SUCH ROUTE"

        number_of_trips = 0
        if stops > max_stops:
            return 0
        number_of_stops = stops  # depth of traversal

        # mark start TownNode as visited
        start.visited = True

        start_edges = self.routes[start]

        for edge in start_edges:
            # here edge.parent_node == start
            if edge.destination == finish:
                # adding to resulting number_of_trips
                #  if edge.destination is the same as we're looking for
                if number_of_stops != max_stops:
                    number_of_trips += 1

            elif not edge.destination.visited:
                number_of_stops = stops + 1  # adding to default value
                number_of_trips += self.count_trips_max_stops(
                    start=edge.destination,
                    finish=finish,
                    max_stops=max_stops,
                    stops=number_of_stops
                )
        start.visited = False  # to make it possible to work with graph again
        return number_of_trips

    def count_trips_fixed_stops(self, start: TownNode,
                                finish: TownNode,
                                fixed_stops: int, stops: int = 0):
        """
        Counts number of possible trips between given Nodes
        :param stops: number of trips
        :param start: first town to start route
        :param finish: last town to finish route
        :param fixed_stops: int of fixed possible stops
        :return: int of trips or "NO SUCH ROUTE"
        """
        if start not in self.routes or finish not in self.routes:
            # can be returned only immediately and not as a result of recursion
            return "NO SUCH ROUTE"

        number_of_trips = 0
        number_of_stops = stops + 1  # depth of traversal

        start_edges = self.routes[start]

        for edge in start_edges:
            # here edge.parent_node == start
            if edge.destination == finish and number_of_stops == fixed_stops:
                # adding to resulting number_of_trips
                #  if edge.destination is the same as we're looking for
                number_of_trips += 1

            elif number_of_stops < fixed_stops:

                number_of_trips += self.count_trips_fixed_stops(
                    start=edge.destination,
                    finish=finish,
                    fixed_stops=fixed_stops,
                    stops=number_of_stops
                )

        return number_of_trips

    def shortest_route(self, start: TownNode,
                       finish: TownNode,
                       def_distance: int = 0):
        """
        Calculate the shortest route in terms of distance to travel
        :param def_distance: default value of sum distance
        :param start: start point town
        :param finish: end point town
        :return: int of shortest distance
        """

        if start not in self.routes or finish not in self.routes:
            # can be returned only immediately and not as a result of recursion
            return "NO SUCH ROUTE"

        all_routes = []

        start_edges = self.routes[start]
        start.visited = True

        for edge in start_edges:
            # add weight of edge to the sum distance - current_distance
            current_distance = edge.distance + def_distance

            # here edge.parent_node == start
            if edge.destination == finish:
                # adding to resulting number_of_trips
                #  if edge.destination is the same as we're looking for

                all_routes.append(current_distance)
                start.visited = False

            elif not edge.destination.visited:
                new_shortest_route = self.shortest_route(
                    start=edge.destination,
                    finish=finish,
                    def_distance=current_distance
                 )

                if new_shortest_route != "NO SUCH ROUTE":
                    all_routes.append(new_shortest_route)

        shortest_route = min(all_routes) if all_routes else "NO SUCH ROUTE"
        start.visited = False  # to make it possible to work with graph again
        return shortest_route

    def count_routes_given_distance(self, start: TownNode, finish: TownNode,
                                    max_distance: int,
                                    distance_def: int = 0):
        """
        Calculates the number of different routes between two points
         with a give maximum distance
        :param distance_def: default traveled distance
        :param max_distance: int
        :param start: TownNode
        :param finish: TownNode
        :return: int or NO SUCH ROUTE
        """

        if start not in self.routes or finish not in self.routes:
            # can be returned only immediately and not as a result of recursion
            return "NO SUCH ROUTE"

        number_of_trips = 0

        start_edges = self.routes[start]

        for edge in start_edges:
            # adding to distance sum
            distance_traveled = edge.distance + distance_def
            # here edge.parent_node == start
            if edge.destination == finish and distance_traveled < max_distance:
                # adding to resulting number_of_trips
                #  if edge.destination is the same as we're looking for
                number_of_trips += 1

            if distance_traveled < max_distance:
                number_of_trips += self.count_routes_given_distance(
                    start=edge.destination,
                    finish=finish, max_distance=max_distance,
                    distance_def=distance_traveled
                )

        return number_of_trips
