paths = {}

while 1:
    src, dst = input()
    if src == '*': break
    if src in paths:
        paths[src].append(dst)
    else:
        paths[src] = [dst]
    if dst in paths:
        paths[dst].append(src)
    else:
        paths[dst] = [src]


def bfs(src, dst, no_visit=None, path=[]):
    if src == dst:
        return [path + [src]]

    if src == no_visit:
        return []

    if src in path:
        return []

    connection_paths = []

    for connection in paths[src]:
        connection_path = bfs(connection, dst, no_visit, path + [src])

        if connection_path:
            connection_paths += connection_path

    return connection_paths

print(bfs('A', 'B'))
