#1 桁の数字が表示される画面と、ボタンからなる機械があります。画面に数字kが表示されているとき、
# ボタンを 1 回押すと画面の数字がakに変わります。
# 0 が表示されている状態からボタンを 3 回押すと、画面には何が表示されますか？




a = list(map(int,input().split()))

k = 0 #最初に画面に表示されているのは0     #print(a[a[a[0]]])
k = a[k] #ボタンを押す 
k = a[k] #ボタンを押す
k = a[k] #ボタンを押す

print(k)