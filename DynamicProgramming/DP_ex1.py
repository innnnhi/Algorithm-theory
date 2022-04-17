# 개미 전사
# 4
# 1 3 1 5
# 해설 전
# 문제점 : 최적의 해를 구하는 경우의수가 항상 모든 창고를 다 털어야만 나오는 것은 아님 (예를 들어 0 3 10 5) 가 있으면 2,4번 창고를 한번에 터는것 보다
# 3번창고(10)하나만을 터는 것이 더 최적값이므로 모든 경우의수 설정시 유의
n = int(input())
garage = list(map(int, input().split()))

dp = []
even = 0
odd = 0
for i in range(n):
    if i % 2 == 0:
        even += garage[i]
    else :
        odd += garage[i]
    dp.append(odd)
    dp.append(even)
print(max(dp))