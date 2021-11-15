n, k = map(int, input().split())
count = 0

while True:
    #(N==K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k) * k
    count += (n - target)
    n = target
    #N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    #K로 나누기
    count += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
count += (n-1)
print(count)

'''
n, k = map(int, input().split())
count = 0

while n >= k: #N이 K이상이라면 K로 계속 나누기
    while n % k != 0: #N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
        n-=1
        count+=1
    n //= k
    count+=1

while n>1: #마지막 남은 수에 대하여 1씩 빼기 
    n-=1
    count+=1

print(count)
'''
