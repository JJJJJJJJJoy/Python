a=input()

x,y=0,0

for s in a :

 if s=="U":
   y +=1
  
 elif s=="D":
   y -=1
  
 elif s=="L":
   x -=1

 elif s=="R":
   x +=1


if x==0 or y==0 :
   print("Y")
else:
   print("N")
