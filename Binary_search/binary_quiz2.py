# 정렬된 배열에서 특정 수의 개수 구하기
# o(logN) 시간복잡도 ==> 이진탐색 이용해야함

# 표준 라이브러리 이용 방식
from bisect import bisect_left, bisect_right
# 7 2
# 1 1 2 2 2 2 3

n, x = map(int, input().split())
arr = list(map(int, input().split()))


def using_library_sol(arr, left, right):
    left_index = bisect_left(arr, left)
    right_index = bisect_right(arr, right)
    return right_index - left_index


answer = using_library_sol(arr, x, x)

if answer == 0:
    print(-1)
else:
    print(answer)
