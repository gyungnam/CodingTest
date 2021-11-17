p = input() #나이트 현재 위치
x = ord(p[0]) - ord('a') + 1
y = int(p[1])

#나이트가 이동할 수 있는 8가지 방향
dir = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

#8가지 방향에 대해 이동 가능한지 확인
count = 0
for d in dir:
    nx = x+d[0]
    ny = y+d[1]
    if(nx>=1 and ny>=1 and nx<=8 and ny<=8):
        count+=1

print(count)