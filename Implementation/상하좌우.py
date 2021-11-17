n = int(input())
plans = input().split()
x, y = 1, 1

#L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
dir = ['L', 'R', 'U', 'D']

for plan in plans: #이동 계획 하나씩 확인
    for i in range(len(dir)): #이동 후 좌표 구하기
        if plan == dir[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: #공간 벗어나면 경우 무시
        continue

    x,y = nx, ny #이동 수행

print(x, y)