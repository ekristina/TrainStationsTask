__author__ = "ekristina"

import cmd
from collections import defaultdict

from definitions import TownNode, DistanceEdge, RouteGraph


def make_default_graph():
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
    return graph


class TrainService(cmd.Cmd):

    def __init__(self):
        super().__init__()
        print("Start by adding towns and distances: add_route"
              "\nTo see available commands type 'help' or '?'\n"
              "To exit press command+D (Mac) or ctrl+D (Linux)")

    graph = defaultdict(list)

    def do_add_route(self, line):
        """Add two towns to database and the distance between them"""
        print("Do you want to use default graph or enter your own?\n"
              "Type 'default' or 'my'")
        answer = input()
        if answer == 'default':
            self.graph = make_default_graph()

        elif answer == 'my':

            print("Enter first town name: ")
            first_town = TownNode(input())

            print(f"First town {first_town} has been saved\n"
                  f"Enter second town name: ")
            second_town = TownNode(input())

            print(f"Second town {second_town} has been saved\n"
                  f"Enter distance between two cities: ")
            distance = int(input())
            self.graph[first_town].append(
                DistanceEdge(first_town, second_town, weight=distance)
            )

            print(f"Thank you, the route {first_town}{second_town}{distance}"
                  f" has been saved.\n Would you like to add more? (y/n)")

            answer = input()
            while answer not in ['y', 'n']:
                print("Please enter 'y' or 'n': \n"
                      "If you want to exit press command+D")
                answer = input()

            if answer == 'y':
                self.do_add_route(line)

        else:
            self.do_add_route(line)

        print("All the towns have been saved to the 'graph' dict")

    def do_calculate_distance(self, route):
        """Calculates distances between towns.
        Type desired as such: A-B-C"""
        if not route:
            print("Type desired route in format: A-B-C")
            towns = input().split("-")
        else:
            towns = route.split("-")

        towns = [TownNode(town) for town in towns]
        result = RouteGraph(routes=self.graph).count_full_distance(towns)
        print(f"The distance is {result}")

    def do_show_graph(self, _):
        """Shows Towns and distances inside the graph"""
        print("Representation of the graph:")
        print(dict(self.graph))  # dict because it can be a defaultdict

    def do_count_trips_max_stops(self, line):
        """Counts the number of trips given maximum number of stops
        ** Use calculate_num_trips_max_stops with parameters:
                <start> - start_point
                <finish> - end_point
                <maximum number of stops>
        """
        parameters = line.split()
        if line:

            if len(parameters) != 3:
                print("Wrong number of arguments")

            else:
                start, finish, max_number = parameters
                start = TownNode(start)
                finish = TownNode(finish)
                max_number = int(max_number)

        if not parameters or len(parameters) != 3:

            print("Enter start point: ")
            start = TownNode(input())

            print("Enter finish point: ")
            finish = TownNode(input())

            print("Enter max number of stops: ")
            max_number = int(input())

        result = RouteGraph(routes=self.graph).count_trips_max_stops(
                start, finish, max_number
            )

        print(f"Number of trips from {start} to {finish} "
              f"given {max_number} max stops is {result}")

    def do_count_trips_exact_stops(self, line):
        """Counts the number of trips given exact number of stops
        ** Use calculate_num_trips_max_stops with parameters:
                <start> - start_point
                <finish> - end_point
                <exact number of stops>
        """
        parameters = line.split()
        if line:

            if len(parameters) != 3:
                print("Wrong number of arguments")

            else:
                start, finish, exact_number_of_stops = parameters
                start = TownNode(start)
                finish = TownNode(finish)
                exact_number_of_stops = int(exact_number_of_stops)

        if not parameters or len(parameters) != 3:

            print("Enter start point: ")
            start = TownNode(input())

            print("Enter finish point: ")
            finish = TownNode(input())

            print("Enter max number of stops: ")
            exact_number_of_stops = int(input())

        result = RouteGraph(routes=self.graph).count_trips_fixed_stops(
                start, finish, exact_number_of_stops
            )

        print(f"Number of trips from {start} to {finish} "
              f"given {exact_number_of_stops} exact number "
              f"of stops is {result}")

    def do_shortest_route(self, line):
        """Calculates the shortest route between two points
            in terms of distance
        ** Use shortest_route with parameters:
                <start> - start_point
                <finish> - end_point
        """

        parameters = line.split()
        if line:

            if len(parameters) != 2:
                print("Wrong number of arguments")

            else:
                start, finish = parameters
                start = TownNode(start)
                finish = TownNode(finish)

        if not parameters or len(parameters) != 2:
            print("Enter start point: ")
            start = TownNode(input())

            print("Enter finish point: ")
            finish = TownNode(input())

        result = RouteGraph(routes=self.graph).shortest_route(
            start, finish
        )
        print(f"The shortest distance from {start} to {finish} is {result}")

    def do_EOF(self, _):
        # to have an option of properly terminate program
        return True


if __name__ == "__main__":
    TrainService().cmdloop()
