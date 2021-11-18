array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #j가 i부터 1까지 1씩 감소
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

'''range의 매개 변수는 3개 (start, end, step) 
3번째 매개 변수인 step에 -1이 들어가면 
start 인덱스부터 시작해서 end+1 인덱스까지 1씩 감소한다. '''

print(array)
