import re
import pprint

# parse a containment rule into a ContainmentRule struct. Return a dict of
# "container" that's a string describing the color to a list of tuples where item 0 is amount, item 2 is color
def parse_containment_rule(string):
    return_dict = dict()

    ruleparts = string.split("contain")
    parts = [string_without_bags(part).strip() for part in ruleparts]

    return_dict["container"] = parts[0]
    if parts[1] == "no other":
        return_dict["contained"] = []
    else:
        return_dict["contained"] = [(int(bag.strip().split(" ")[0]), " ".join(bag.strip().split(" ")[1:])) for bag in parts[1].split(",")]

    return return_dict

# strips the "bag" or "bags" or "bags." or "bag." part of the rule
def string_without_bags(string):
    return re.sub(" bags*\.*", "", string)

def immediate_containers_for_color(color, rules):
    result = list()
    for rule in rules:
        for contained in rule["contained"]:
            if contained[1] == color:
                result.append(rule["container"])
    return result

def all_containers_for_color(color, rules, current_set):
    containers = immediate_containers_for_color(color, rules)
    for container in containers:
        current_set.add(container)
        all_containers_for_color(container, rules, current_set)
    return current_set

# return all the bags that must be contained in the passed-in color
def all_contained_bags(color, rules):
    return_list = []
    for rule in rules:
        if rule["container"] == color:
            for bag in rule["contained"]:
                for copy in range(0,bag[0]):
                    return_list.append(bag[1])
                    return_list.extend(all_contained_bags(bag[1], rules))
    return return_list


if __name__ == '__main__':
    data = '''
    light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
'''

    parsed = [parse_containment_rule(line) for line in data.split("\n") if len(line) > 0]
    pprint.pprint(all_contained_bags('shiny gold', parsed,))
