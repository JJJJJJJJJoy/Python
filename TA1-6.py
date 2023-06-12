y=int(input())

if y%4>=1 :
  print("False")
elif y%4==0 and y%100>=1 : 
  print("True")
elif y%4==0 and y%400==0:
  print("True")
else :
  print("False")