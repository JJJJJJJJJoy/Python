n=int(input())

c=0

while n>0 :
     if n % 2 == 0 :
        n /=2
        c +=1
        continue

     else :
        n >=1
        n -=1
        c +=1
        continue
        
print(c)