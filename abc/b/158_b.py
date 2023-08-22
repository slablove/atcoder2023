from re import A


N, blue, red = map(int,input().split())
T = blue + red
# n / (blue + red) = q...r
q, r = N // T, N % T
#q, r = divmod(N, T)
ans = blue * q + min(blue, r)
print(ans)

#n,a,b = map(int, input().split())
#ans = n // (a+b)
#ans *= a
#if n % (a+b) != 0:
#   ans += min(a,n%(a+b))
#print(ans)