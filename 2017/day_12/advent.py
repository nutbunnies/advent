connections = {}
with open("input.txt", "r") as file:
    for connection in file.read().strip().split("\n"):
        src, dests = connection.split(" <-> ")
        connections[int(src)] = list(map(int, dests.split(", ")))

def walk_connections(node_id, visited):
    visited.add(node_id)
    for node in connections[node_id]:
        if not node in visited:
            walk_connections(node, visited)

from_root = set()
walk_connections(0, from_root)
print("nodes connected to node 0: ", len(from_root))

group_count = 0
visited_overall = set()
for node_id in range(0, len(connections)):
    if not node_id in visited_overall:
        walk_connections(node_id, visited_overall)
        group_count += 1

print("total groups: :", group_count)

