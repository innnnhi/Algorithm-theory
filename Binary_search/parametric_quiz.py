# 떡 자르기
# 4 6
# 19 15 10 17
import math
n , m = map(int, input().split())
arr = list(map(int, input().split()))
use_data = sorted(arr)
target = []


def sol(arr):
    # answer = 0
    for i in use_data:
        answer = 0
        for j in arr:
            answer += (j - i)
        target.append(answer)
    return target


min_differ = 99999
index = 0
for u in target:
    differ = math.fabs(m-u)
    if differ < min_differ:
        min_differ = differ
        index += 1
print(arr[index - 1])

