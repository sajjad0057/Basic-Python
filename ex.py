'''
graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}
visited = []


def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=' ')
        visited.append(node)
        for x in graph[node]:
            dfs(visited, graph, x)


dfs(visited, graph, 'A')


def toh(n, s, a, d):
    if n == 1:
        print('move disk 1 from ', s, ' to ', d)
        return
    toh(n - 1, s, d, a)
    print('move disk', n, 'from', s, 'to', d)
    toh(n - 1, a, s, d)


toh(3, 'A', 'B', 'C')

'''
'''
graph = {
    'A': ['B', 'S'],
    'B': ['A'],
    'C': ['D', 'E', 'F', 'S'],
    'D': ['C'],
    'E': ['C', 'H'],
    'F': ['C', 'G'],
    'G': ['F', 'S'],
    'H': ['E', 'G'],
    'S': ['A', 'C', 'G']
}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=' ')
        for x in graph[s]:
            if x not in visited:
                visited.append(x)
                queue.append(x)

bfs(visited,graph,'A')
'''

graph = [
    [0, 16, 11, 6],
    [8, 0, 13, 16],
    [4, 7, 0, 9],
    [5, 12, 2, 0]
]
n = 4
visited = (1 << n) - 1


def checkTsp(mask, pos):
    if mask == visited:
        return graph[pos][0]
    ans = 9999999999
    for city in range(n):
        if (mask & (1 << city)) == 0:
            newAns = graph[pos][city] + checkTsp(mask | (1 << city), city)
            ans = min(ans, newAns)
    return ans


print(checkTsp(1, 0))

