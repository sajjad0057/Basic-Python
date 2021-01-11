graph = {
    '0': ['1', '2','3'],
    '1':[],
    '2': ['4','5'],
    '3':['6'],
    '4':[],
    '5':[],
    '6':[]
}
visited = []


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.append(node)
        for x in graph[node]:
            dfs(visited, graph, x)


dfs(visited, graph, '0')
