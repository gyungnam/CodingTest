n, m = map(int, input().split())
x, y, dir = map(int, input().split())

#방문한 위치를 저장하기 위한 맵을 생성하기 위해 0으로 초기화
d = [[0]*m for _ in range(n)]
d[x][y] = 1 #현재 좌표 방문 처리

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def turn_left():
    global dir
    dir -= 1
    if dir == -1: #북쪽에서 왼쪽으로 회전하면 서쪽임
        dir = 3

count = 1
turn_times = 0

while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_times = 0
        continue
    else:
        turn_times += 1
    
    if turn_times == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break

        #turn_times = 0

print(count)