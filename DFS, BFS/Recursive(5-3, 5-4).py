def recursive_funtion(i):
    if i == 10:
        return
    print(i, '번째 재귀 함수에서', i+1, '번 째 재귀함수를 호출합니다.')
    recursive_funtion(i+1)
    print(i, '번 째 재귀 함수를 종료합니다.')
recursive_funtion(1)

''' #종료 조건 없음
def recursive_function():
    print('재귀 함수를 출력합니다.')
    recursive_function()

recursive_function()
'''