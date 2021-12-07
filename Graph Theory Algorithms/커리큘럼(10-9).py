from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time) # 리스트의 값을 복제
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for next in graph[now]: 
            result[next] = max(result[next], result[now] + time[next]) 
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, v+1):
        print(result[i])
        
topology_sort()