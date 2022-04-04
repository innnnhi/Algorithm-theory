# 삽입 정렬 (insertion sort)
# arr = [1, 10, 3, 9, 7, 12]
# arr = [1, 10 , 5, 8, 7, 6, 4, 3, 2, 9]
# arr = [2, 3, 4, 5, 6, 1]
arr = [x for x in range(0,100)]
# 각 숫자를 "적절한 위치에 ""필요할 때만"" 삽입 하는 방법" 으로 문제 해결
# 앞의 정렬은 이미 제대로 정렬 되어 있다고 '가정'하고 삽입될(정렬될) 원소를 살펴볼 때
# 필요한 만큼만 이동해서 순서에 맞게 삽입되면 된다.

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break
print(arr)
