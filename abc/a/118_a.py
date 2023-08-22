A,B = map(int,input().split())

if B%A == 0:
    print(A+B)
else:
    print(B-A)
    

#print(A+B if B%A==0 else B-A)
#A,B = list(map(int,input().split()))
