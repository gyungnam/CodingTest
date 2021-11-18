def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    #현재 노드와 연결된 다른 노드의 방문 여부 확인 후 없으면 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [], 
    [2, 3, 8], 
    [1, 7], 
    [1, 4, 5],
    [3, 5],
    [3, 4], 
    [7],
    [2, 6, 8],
    [1, 7]
]

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
#인덱스를 0부터가 아닌 1부터 사용하기 위해 1칸 더 할당
visited = [False] * 9

dfs(graph, 1, visited)