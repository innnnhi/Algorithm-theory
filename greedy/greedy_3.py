import time
# 100000000000 23
# 2연산중 하나를 택함, 단 두번째 연산은 n % k == 0 일때 사용가능
# 1. n-1 // 2. n // k
start_time = time.time()
n, k = map(int, input().split())
## 1
cnt = 0
# while n >= k :
#     while n % k != 0:
#         n -= 1
#         cnt += 1
#     n = n // k
#     cnt += 1
#
# while n > 1:
#     n -= 1
#     cnt += 1
# print(cnt)
# end_time = time.time()
# print("time1 : " ,end_time - start_time ) # time1 :  1.981036901473999 // 127


## 2
# while n != 1 :
#     if n % k == 0: k의 배수일때
#         n = n // k
#         cnt += 1
#     else :
#         n = n - 1
#         cnt += 1
# print(cnt)
# end_time = time.time()
# print("time2 : " ,end_time - start_time )  #time2 :  27.14470911026001 // 127

## 3

# while True: # n27 k4
#     target = (n//k) * k # n = k배수 24
#     cnt += (n-target) # cnt = 3(1씩 3번 빼주)
#     n = target # 24
#
#     if n < k :
#         break
#     cnt += 1
#     n = n // k
# cnt += (n-1)
# print(cnt)
# end_time = time.time()
# print("time3 : ", end_time - start_time) # time3 :  1.3185629844665527 // 127