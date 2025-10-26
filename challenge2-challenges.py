import timeit

setup = """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
 
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""

locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

def nested_loop():
    result = []
    locations_to_forest =[(location, description) for location, description in locations.items()
                          if location in [number for number, directions in exits.items() if 5 in directions.values()]]
    for x in locations.keys():
        y = [number for number, directions in exits.items() if x in directions.values()]
        result.append(locations_to_forest)
    return result


def nested_gen():
    result = []
    locations_to_forest =((location, description) for location, description in locations.items()
                          if location in [number for number, directions in exits.items() if 5 in directions.values()])
    for x in locations.keys():
        y = [number for number, directions in exits.items() if x in directions.values()]
        result.append(locations_to_forest)
    return result


print(nested_loop())
print(nested_gen())
result_1 = timeit.timeit(nested_loop, setup, number=1000)

print("Nested loop:\t{}".format(result_1))
print("Nested gen:\t{}".format(result_1))
