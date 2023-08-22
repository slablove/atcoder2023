K = int(input())
A,B = map(int,input().split())
flag = 0
for i in range(A,B+1):
    if i%K == 0:
        flag = 1
        break
if flag == 1:
    print("OK")
else:
    print("NG")

#k=int(input())a,b=map(int, input().split())if (a-1)//k!=b//k: print("OK") else print("NG")
#K = int(input()) A, B = [int(i) for i in input().split()] i = 0; while K*i<=B: if K*i>=A: print("OK") exit() i=i+1 print("NG")
