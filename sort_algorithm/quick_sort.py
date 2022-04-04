# 퀵 정렬 : 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.
# 일반적인 상황에서 가장 많이 사용되는 정렬알고리즘
# 병합정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준데이터(pivot)으로 설정함.
#                                                 i) 엇갈리지 않으면 고른 두 수의 위치(인덱스)를 바꾼다
# 퀵 정렬을 진행하면서(피벗을 기준으로) 큰 값/ 작은 값 찾는데 ii)엇갈린다면 작은값과 피벗과의 위치를 바꿔준더
# iii) 그렇다면 바뀐피벗을 중심(기준)으로 , 왼쪽값은 피벗보다 작은 값들만, 오른쪽은 큰값들만 정렬됨. (그룹 2개가 생김 == 분할)
# iv) 1그룹 , 2그룹 따로 피벗들을 설정해주고(첫번째 원소들) 반복적으로 퀵정렬을 구현


arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# print(arr)

def quick_sort(arr, start, end):
    if start >= end:
        return arr
    pivot = start
    found_big = start + 1
    found_small = end

    while found_big <= found_small:
        while found_big <= end and arr[found_big] <= arr[pivot]:
            found_big += 1
        while found_small > start and arr[found_small] >= arr[pivot]:
            found_small -= 1
        # 6, 5
        if found_big > found_small:
            # arr[pivot], arr[found_small] = arr[found_small], arr[pivot]
            temp = arr[pivot]
            arr[pivot] = arr[found_small]
            arr[found_small] = temp
            # print(arr, found_big, found_small, '피벗 ㄱ')
        else:
            # arr[found_big], arr[found_small] = arr[found_small], arr[found_big]
            temp = arr[found_small]
            arr[found_small] = arr[found_big]
            arr[found_big] = temp
            # print(arr, found_big, found_small, '서로 ㄱ')
    quick_sort(arr, start, found_small - 1)  # 1
    quick_sort(arr, found_small + 1, end)  # 2
    return arr


print(quick_sort(arr, 0, len(arr) - 1))
