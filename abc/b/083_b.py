n, a, b = list(map(int, input().split())) 

ans = 0

for i in range(1, n+1):
  digitSum = sum(list(map(int, str(i))))
  if (digitSum >= a and digitSum <= b):
    ans += i

print(ans)

#N, A, B = map(int, input().split())

#answer = 0

#for i in range(N+1):
#  s = str(i) # 数字の20を文字の20に変える 
#  n_list = list(map(int, s)) # 右のlist(~で配列を宣言し、map関数で文字列sをintに変換
#  summary = sum(n_list)

#  if A <= summary <= B # summaryがA以上B以下の時、足す
#       answer += i

#print(answer)


#13,14,,,などの数字は1+3、1+4,,,と足す必要がある。
#数字のままでは13を1と3に分解することができないので、13を一度文字列に変えて1と3に変更する→数字に戻して1と3を足し合わせる必要がある。#