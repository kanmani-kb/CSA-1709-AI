
colors = ['Red', 'Green', 'Blue']

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

result = {}

def solve(region):
    if region == len(graph):
        return True

    node = list(graph.keys())[region]

    for color in colors:
        safe = True

        for neighbor in graph[node]:
            if result.get(neighbor) == color:
                safe = False
                break

        if safe:
            result[node] = color

            if solve(region + 1):
                return True

            del result[node]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for node, color in result.items():
        print(node, ":", color)
else:
    print("No solution")
