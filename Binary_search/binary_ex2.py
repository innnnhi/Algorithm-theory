# 이진탐색 반복문 구현

n , target = list(map(int, input().split()))
arr = list(map(int, input().split()))


def binery_serch_repetitive(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


result = binery_serch_repetitive(arr, target, 0, n-1)

if result is None:
    print("원소 없음")
else :
    print(result + 1)
