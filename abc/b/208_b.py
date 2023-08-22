n = int(input())

sum = 0 #  合計点を表す変数
i = 0 #カウンタ変数


while i < n:
    x = int(input()) #合計点を表す変数sumを作っておきループするたびに入力変数xに入れsumに足しています
    sum += x
    i += 1
print(sum)
