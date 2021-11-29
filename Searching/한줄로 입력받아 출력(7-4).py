import sys

#하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

#readline()은 기본적으로 개행문자 포함
#strip(): 왼쪽, 오른쪽 공백을 삭제 - lstrip(left), rstrip(right)

print(input_data)