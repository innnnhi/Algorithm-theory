# 떡볶이 문제 이진탐색 이용
# 큰 탐색범위를 보았을때 이진탐색을 떠올려야함
# "현재 이 높이로 자르면 조건을 만족할 수 있는가 ?" 를 확인한 뒤에 '조건의 만족 여부(예 or 아니오)에
# 따라서 탐색 범위를 좁혀서 해결할 수 있다.

# 떡의 개수(n) 요청한 떡의 길이(m)을 입력
n , m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보 입력
arr = list(map(int, input().split()))

start = 0
end = max(arr) # 가장 긴 떡의 끝부분이 끝점으로 설정

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0 # 잘려진 떡의 양
    mid = (start + end) // 2 # mid == 자르는 떡의 높이 ; 우리가 구하고자 하는 값
    for x in arr:
        # 잘랐을 때의 떡의 양 계산
        if x > mid :
            total += (x - mid)

    # 떡의 양이 고객이 원하는 양(m)보다 작다면 더 많이 자르기 (왼쪽 부분 탐색)
    if total < m :
        end = mid - 1
    # 떡의 양이 충분하다면 덜 자르기 --> 그러면서 최적의 값을 찾아야하니 result 에 값 저장 (오른쪽 값 탐색)
    else :
        result = mid
        start = mid + 1

print(result)