# arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
# arr = [100, 200, 1, 42, 32]
arr = [x for x in range(0,10000)]
# 버블 정렬 : 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보내는 정렬 방법
# 구현하기에는 굉장히 쉽지만 효율성이 가장 떨어지는 알고리즘
# 한번의 반복이 끝났을 때 "선택정렬"과는 반대로 가장 큰값이 가장 멀리 보내지게 된다.

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr))



