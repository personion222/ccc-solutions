roads = {}
road_names = set()

while 1:
    src, dst = input()
    if src == '*': break

    road_names.add(src + dst)

    if src in roads:
        roads[src].append(dst)
    else:
        roads[src] = [dst]
    if dst in roads:
        roads[dst].append(src)
    else:
        roads[dst] = [src]


def bfs(src, dst, no_visit=None, path=[]):
    if src == dst:
        return [join_paths(path + [src])]

    if src == no_visit:
        return []

    if src in path:
        return []

    connection_roads = []

    for connection in roads[src]:
        connection_path = bfs(connection, dst, no_visit, path + [src])

        if connection_path:
            connection_roads += connection_path

    return connection_roads

def join_paths(points):
    joined_path = []
    for idx, point in enumerate(points[:-1]):
        order_1 = point + points[idx + 1]
        order_2 = points[idx + 1] + point
        if order_1 in road_names:
            joined_path.append(order_1)
        else:
            joined_path.append(order_2)

    return joined_path


paths = bfs('A', 'B')
disconnecting_candidates = set(paths[0])
disconnecting = set(paths[0])

for path in paths[1:]:
    for road in disconnecting_candidates:
        if road not in path and road in disconnecting:
            disconnecting.remove(road)

for disconnecting_road in disconnecting:
    print(disconnecting_road)
print(f"There are {len(disconnecting)} disconnecting roads.")
