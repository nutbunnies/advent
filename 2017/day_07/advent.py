from collections import namedtuple
import re

inputs = """padx (45) -> pbga, havc, qoyq
xhth (57)
ebii (61)
havc (66)
ktlj (57)
tknk (41) -> ugml, padx, fwft
fwft (72) -> ktlj, cntj, xhth
ugml (68) -> gyxo, ebii, jptl
qoyq (66)
jptl (61) -> xxxx
gyxo (61)
xxxx (0)
cntj (57)
pbga (66)"""

inputs = ""
file = open("input.txt", "r")
for line in file:
    inputs += line
file.close()
inputs = inputs.strip()

names = set()
children = set()
p = re.compile(r"(\w+) \((\d+)\)[\s\-\>]?(.*)")

for input in inputs.split("\n"):
    m = p.match(input)
    names.add(m.group(1))
    sub_parts = m.group(3)
    if sub_parts != "":
        for part in sub_parts[3:].split(", "):
            children.add(part)

print(len(names))
print(len(children))

base = names.difference(children).pop()
print("bottom: {}".format(base))
print()

programs = []

class Program(object):
    def __init__(self, name, weight, children=set(), total_weight=0):
        self.name = name
        self.weight = weight
        self.children = children
        self.total_weight = total_weight

    def __str__(self):
        return "{} {} ({}) {}".format(self.name, self.weight, self.total_weight, self.children)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "name: {}, weight: {}, total_weight: {} {}".format(self.name, self.weight, self.total_weight, self.children)

    def __hash__(self):
        return self.name.__hash__()

program_defs = []
for input in inputs.split("\n"):
    program_defs.append(input)

def find_program_def(progs, program_name):
    for prog in progs:
        if prog.startswith(program_name):
            return prog

def parse_def(prog):
    m = p.match(prog)
    name = m.group(1)
    weight = m.group(2)
    sub_programs = m.group(3)
    program = Program(name, int(weight), set(), 0)
    if sub_programs != "":
        for sub_prog in sub_programs[3:].split(", "):
            sub_prog_line = find_program_def(program_defs, sub_prog)
            child = parse_def(sub_prog_line)
            program.children.add(child)
            # program.total_weight += child.weight

    return program

def weight_tree(node):
    node.total_weight += node.weight
    for sub_node in node.children:
        weight_tree(sub_node)
        node.total_weight += sub_node.total_weight


base_prog = find_program_def(program_defs, base)
print(base_prog)
tree = parse_def(base_prog)
# print(tree)

def print_tree(node, indent):
    for child in node.children:
        print("{}name: {}, node_weight: {}, total weight: {}".format(indent, child.name, child.weight, child.total_weight))
        print_tree(child, "{}\t".format(indent))

# print()
weight_tree(tree)

# print()
# print()
# print("name: {}, node_weight: {}, total weight: {}".format(tree.name, tree.weight, tree.total_weight))
# print_tree(tree, "")