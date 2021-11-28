def binary_search(array, m, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for x in array:
            #잘랐을 때 떡의 양 계산
            if x > mid:
                total += x - mid
        #떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        if total < m:
            end = mid - 1
        #떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        else:
            result = mid #최대한 덜 잘랐을 때가 정답이므로, 결과값 저장
            start = mid + 1
    return result

#떡의 개수(n)와 요청한 떡의 길이(m)을 입력받기            
n, m = map(int, input().split())
#각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

print(binary_search(array, m, 0, max(array)))