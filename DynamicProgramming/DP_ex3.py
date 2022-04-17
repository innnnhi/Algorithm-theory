# 화폐구성

# ai = 금액 i를 만들수 있는 최소한의 화폐개수
# K = 각 화폐의 단위
# 점화식 : 각 화폐단위인 k를 하나씩 확인하며
# - ai-k 를 만드는 방법이 존재하는 경우 : ai = min(ai, ai-k +1)
# - ai-k 를 만드는 방법이 존재하지 않는 경우 : ai = INF

# 정수 n,m입력받기
n, m = map(int, input().split())
# n개의 화폐단위 정보 입력받기
array = []
for _ in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 dp테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n): # i == 각각의 화폐단위
    for j in range(array[i], m+1): # j == 각각의 금액
        # 각각의 화폐단위를 하나씩 확인하면서 그때마다 모든 금액을 확인하며 각 금액에 대한 옵티멀솔루션(최적해) 값을 갱신하도록 함 ==> 다이나믹프로그래밍
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])