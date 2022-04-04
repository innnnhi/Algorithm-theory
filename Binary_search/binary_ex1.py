# binery_serch 재귀적 구현

def binery_serch_recursive(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 중간점값 == 타겟값 이면 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간값 > 타겟값이면 중간값기준 오른쪽은 볼필요 없음 -> 새로운 끝점(중간값 왼쪽 값) 지정-> mid-1
    elif arr[mid] > target:
        return binery_serch_recursive(arr, target, start, mid - 1)
    # 중간값 < 타겟값이면 중간값기준 왼쪽은 볼필요 없음 - > 새로운 시작점(중간값 오른쪽 값) 지정 -> mid +1
    else:
        return binery_serch_recursive(arr, target, mid + 1, end)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binery_serch_recursive(arr, target, 0, n - 1)

if result == None:
    print("원소 존재 하지 않음")
else:
    print(result + 1)
