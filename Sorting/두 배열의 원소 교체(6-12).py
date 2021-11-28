n, k = map(int, input().split())
a = list(map(int, input().split())) #배열 A
b = list(map(int, input().split())) #배열 B

a.sort() #A는 오름차순
b.sort(reverse=True) #B는 내림차순

#첫 번째 인덱스부터 확인하며 두 배열의 원소를 최대 K번 비교
for i in range(k):
    #A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        #두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: #A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))