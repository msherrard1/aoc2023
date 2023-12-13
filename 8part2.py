from datetime import datetime
import re
import math
startTime = datetime.now()

def parse(input_data):
    lines = input_data.splitlines()
    
    left_right = lines[0]

    nodes = {}
    pattern = re.compile(r'^(\w{3}) = \((\w{3}), (\w{3})\)$')

    for node_entry_line in lines[2:]:
        matches = pattern.findall(node_entry_line)[0]
        nodes[matches[0]] = (matches[1],matches[2])

    return left_right, nodes

def traverse_nodes(starting_node, left_right, nodes):
    current_node = starting_node
    steps_taken = 0

    while current_node[-1] != 'Z':
        for direction in left_right:
            steps_taken += 1
            if direction == "L":
                current_node = nodes[current_node][0]
            if direction == "R":
                current_node = nodes[current_node][1]
            if current_node[-1] == "Z":
                return steps_taken

def traverse_multiple_nodes(left_right, nodes):
    starting_nodes = [node for node in nodes.keys() if node[-1] == 'A']
    steps_needed = []

    for starting_node in starting_nodes:
        steps_needed.append(traverse_nodes(starting_node,left_right,nodes))

    return math.lcm(*steps_needed)    

if __name__ == "__main__":
    with open('8input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""

#     input_data ="""LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

#     input_data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

    left_right, nodes = parse(input_data)
    print(traverse_multiple_nodes(left_right,nodes))
    print(datetime.now() - startTime)