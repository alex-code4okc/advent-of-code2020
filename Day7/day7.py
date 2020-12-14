import re
import networkx as nx

number = re.compile("\d{1,}")


def recursive_descent(d: dict, collector: set, start_key: str) -> set:
    if d.get(start_key):
        for key in d.get(start_key):
            collector.add(key)
            recursive_descent(d, collector, key)
        return collector
    else:
        return collector


def recursive_count(d: dict, collector: list, start_key: str, start_count: int) -> list:
    if d.get(start_key):
        # collector += start
        for key in d.get(start_key):
            next_count = start_count * key[0]
            collector.append(next_count)  # parent * current child
            recursive_count(d, collector, key[1], next_count)
            # current child * children
        return collector
    else:
        return


def result() -> int:
    with open("./Day7/input.txt") as f:
        lines = [line.strip().replace(".", "") for line in f.readlines()]

    bag_DAG = {}

    for line in lines:
        relationships = line.split("contain")
        container = relationships[0].replace(" bags", "").strip()
        contents = []
        if not " no other bags" in relationships[1]:
            contents = relationships[1].split(",")
            for bag in contents:
                bag = bag.replace("bags", "").replace("bag", "").strip()
                number_matches = re.findall(number, bag)
                bag_no = number_matches[0]
                bag_wout_number = bag.replace(bag_no, "").strip()
                bag_no = int(bag_no)
                if bag_DAG.get(container):
                    temp = bag_DAG[container]
                    temp.append((bag_no, bag_wout_number))
                    bag_DAG[container] = temp
                else:
                    bag_DAG[container] = [(bag_no, bag_wout_number)]
        else:
            bag_DAG[container] = contents

    inverse_bag_DAG = {}

    # generate inverse directed acyclic graph
    for key in bag_DAG.keys():
        for values in bag_DAG[key]:
            nkey = values[1]
            if inverse_bag_DAG.get(nkey):
                temp = inverse_bag_DAG[nkey]
                temp.append(key)
            else:
                inverse_bag_DAG[nkey] = [key]

    bags_containing_shiny_gold = recursive_descent(inverse_bag_DAG, set(), "shiny gold")
    total_bags = recursive_count(bag_DAG, [], "shiny gold", 1)
    return len(bags_containing_shiny_gold), sum(total_bags)


r = result()
pass