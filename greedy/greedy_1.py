# 큰수의 법칙

# n= 5, m = 8, k = 3
# 2 4 5 4 6
# print : 46

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
#
# 5 8 3
# 2 4 5 4 6
arr.sort()
first = arr[n-1]
second = arr[n-2]

cnt = (m//(k+1)) * k
cnt += m % (k+1)
print(cnt, 'cnt')

num = 0
num += cnt * first
num += (m-cnt) * second
print(num, '답')
