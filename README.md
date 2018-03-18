### The Problem:  
The local commuter railroad services a number of towns in Kiwiland.  Because of monetary concerns, all of the tracks are 'one-way.' That is, a route from Kaitaia to Invercargill does not imply the existence of a route from Invercargill to Kaitaia.  In fact, even if both of these routes do happen to exist, they are distinct and are not necessarily the same distance!

###### Full description of the problem and needed implementation can be found in __task.txt__ file.


### How To Use

The code was implemented using Python 3.6. No additional libraries required to install.

Use `unittests.py` file for unit tests or `main.py` to add data on-the-go.

All the unit tests have passed:
```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK

```

____

#### Using `main.py`

Run the following in terminal (assuming Python 3 is the default Python version):
```bash
python main.py
```

The first output of the program is:

```
Start by adding towns and distances: add_route
To see available commands type 'help' or '?'
To exit press command+D (Mac) or ctrl+D (Linux)

```

Following the instructions has to be straightforward.

`add_route` command is used to add Nodes - Towns and Edges - Routes along with Weights - Distances.

```
(Cmd) add_route
Do you want to use default graph or enter your own?
Type 'default' or 'my'

```

You can use `default` graph which can be represented as following:

To see what's in a graph type `show_graph'

```
(Cmd) show_graph
Representation of the graph:
{A: [AB5, AD5, AE7], B: [BC4], C: [CD8, CE2], D: [DC8, DE6], E: [EB3]}

```

In the example above keys `A`, `B`, `C`, `D`, `E` are representations of Nodes, values [`AB5`, `AD5`, `AE7`] etc. are representations of Edges with weights.

If you want to create your own graph then type `my` and not `default`, then follow the instructions:

```
(Cmd) add_route
Do you want to use default graph or enter your own?
Type 'default' or 'my'
> my
Enter first town name: 
> King
First town King has been saved
Enter second town name: 
> Queen
Second town Queen has been saved
Enter distance between two cities: 
> 2
Thank you, the route KingQueen2 has been saved.

```

Then you will be asked:

```
 Would you like to add more? (y/n)

```
If you chose `n` you will __not__ be able to add it later.

Now the graph looks like this: 

```
(Cmd) show_graph
Representation of the graph:
{King: [KingQueen2]}
```

To compute the distance between given Towns use `calculate_distance` command. 
You must use the format `A-B-C`.
You may use it as a parameter to `calculate_distance` or pass it later when asked.

```
(Cmd) calculate_distance A-B-C
9
```

```
(Cmd) calculate_distance
Type desired route in format: A-B-C
> A-D
5

```

To count the number of trips between two points with a given maximum number of stops use `count_trips_max_stops <start point> <finish point> <max number of stops>`.

To count the number of trips between two points with a given exact number of stops use `count_trips_exact_stops <start point> <finish point> <exact number of stops>`

```
(Cmd) count_trips_exact_stops A C 4
Number of trips from A to C given 4 exact number of stops is 3
```

To find a shortest route in term of distance use `shortest_route <start> <finish>` command.

```
(Cmd) shortest_route A C
The shortest distance from A to C is 9
```

To find the number of different routes between two towns with a given maximum distance use `count_routes_with_distance <start> <finish> <maximum distance>`
```
(Cmd) count_routes_with_distance C C 30
Number of trips from C to C given maximum distance of 30 is 7
```