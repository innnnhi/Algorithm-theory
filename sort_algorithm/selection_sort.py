# 선택 정렬 : 가장 작은 값을 선택해서 앞으로 보내는 정렬방식

arr = [10, 1, 3 ,7] # 1 3 7 10


for i in range(len(arr)): # 0 1 2 3 = index
    std_index = i # i = 1(10)
    for j in range(i+1, len(arr)): # j == index
        if arr[std_index] > arr[j]:
            std_index = j # std = 0 : 1 2 3

    arr[i], arr[std_index] = arr[std_index], arr[i]

print(arr)





