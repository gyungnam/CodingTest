# 마을을 분할하되, 최소의 비용만으로 마을 안의 각각의 집이 연결되어 있어야함
# 마을 자체를 분할하기 전, 최소의 비용만으로 집을 연결시키기 위해 크루스칼 알고리즘 사용
# -> N개의 집은 N-1개 길만으로 연결됨
# 
# 여기서 임의의 간선 한 개를 뚝 잘라도 1개의 집 자체가 마을이 되고, 최소 신장 트리라는 조건을 만족함
# 
# 따라서, 최소의 비용으로 두 개의 마을을 분할하기 위해서는 가장 큰 비용이 드는 간선 1개를 없애면 됨
# 크루스칼 알고리즘은 비용이 적은 순부터 길을 이어나가기 때문에 가장 마지막에 더한 비용을 빼면 정답


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i
    
edges = []
result = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
last = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)