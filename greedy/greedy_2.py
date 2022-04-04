# m = 열 개수(= 가로 길이) , n = 행 개수(=세로길이)
# 행열 받기

n, m = map(int, input().split())

# target = []
# for i in range(n):
#     a = min(map(int, input().split()))
#     target.append(a)
# print(max(target))

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)