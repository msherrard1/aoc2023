from datetime import datetime
import re
startTime = datetime.now()

def parse(input_data):
    lines = input_data.splitlines()
    
    left_right = lines[0]

    nodes = {}
    pattern = re.compile(r'^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$')

    for node_entry_line in lines[2:]:
        matches = pattern.findall(node_entry_line)[0]
        nodes[matches[0]] = (matches[1],matches[2])

    return left_right, nodes

def traverse_nodes(left_right, nodes):
    current_node = "AAA"
    steps_taken = 0

    while current_node != "ZZZ":
        for direction in left_right:
            steps_taken += 1
            if direction == "L":
                current_node = nodes[current_node][0]
            if direction == "R":
                current_node = nodes[current_node][1]
            if current_node == "ZZZ":
                return steps_taken

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

    left_right, nodes = parse(input_data)
    print(traverse_nodes(left_right,nodes))