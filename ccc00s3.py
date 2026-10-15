import sys
import re

sys.setrecursionlimit(1000000)

n = int(input())
pages = {}
for _ in range(n):
    url = input()
    pages[url] = []
    pages[url].append(input())
    while "</HTML>" != pages[url][-1]:
        pages[url].append(input())

links = {}
for url in pages:
    links[url] = []
    for line in pages[url]:
        link_positions = [match.end() for match in re.finditer("<A HREF=\"", line)]

        for link_position in link_positions:

            page_link = ''
            i = link_position
            while line[i] != '"':
                page_link += line[i]
                i += 1

            links[url].append(page_link)

pairs = []
while 1:
    pairs.append([input()])
    if pairs[-1][0] == "The End":
        pairs.pop(-1)
        break
    pairs[-1].append(input())


def bfs(page, target, route=[]):
    if page == target:
        return True

    if page in route:
        return False

    if page in links:
        for link in links[page]:
            path = bfs(link, target, route + [page])
            if path: return path

    return False

for src, dsts in links.items():
    for dst in dsts:
        print(f"Link from {src} to {dst}")

apostrophe_t = "'t"

for pair in pairs:
    connected = bfs(pair[0], pair[1])
    print(f"Can{apostrophe_t if not connected else ''} surf from {pair[0]} to {pair[1]}.")
