a=input()
b=a.split()


if b[0]=="星期五" or b[0]=="星期六" or b[0]=="星期日":
  print("不開市")

else :
  print(int(b[1])*int(b[2]))