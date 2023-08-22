a,b,c,d = map(int,input().split()) 

#高橋君のモンスターは体力が A で攻撃力が B ,青木君のモンスターは体力が C で攻撃力が D


while True:
    c -= b #c = b -c
    if c <= 0:
        print("Yes")
        exit()
    a -= d # a = d - a
    if a <= 0:
        print("No")
        exit()

#def resolve()
# if __name__ == '__main__': resolve()
#for i in range(101):
#c = c-b if c<=0: print("Yes") break a = a-d if a<=0: print("No") break
