a,b,c = map(int,input().split())

n = a*100 + b*10 + c

#4 3 2 といった入力を432という整数値として解釈する部分を実装　3行目

if n % 4 == 0:
    print("YES")
else:
    print("NO")


#print("YES" if eval(input().replace(" ",""))%4 == 0 else "NO")
# if int(r + g + b) % 4 == 0:
#a = int(''.join(input().split())) print('YES' if a%4 == 0 else 'NO')

