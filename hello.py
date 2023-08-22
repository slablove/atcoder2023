s=input()
flag=False
for i in range(len(s)):
  if s[i]=="h" and s[i+1] == "i":
  	flag=True
if flag==True:
  print("Yes")
else:
  print("No")
 
