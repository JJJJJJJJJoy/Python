n=input()

c=0

if n[0]=='A': 
  c+=1+0*9
elif n[0]=='B':
  c+=1+1*9
elif n[0]=='C':
  c+=1+2*9
elif n[0]=='D':
  c+=1+3*9
elif n[0]=='E':
  c+=1+4*9
elif n[0]=='F':
  c+=1+5*9
elif n[0]=='G':
  c+=1+6*9
elif n[0]=='H':
  c+=1+7*9
elif n[0]=='I':
  c+=3+4*9
elif n[0]=='J':
  c+=1+8*9
elif n[0]=='K':
  c+=1+9*9
elif n[0]=='L':
  c+=2+0*9
elif n[0]=='M':
  c+=2+1*9
elif n[0]=='N':
  c+=2+2*9
elif n[0]=='O':
  c+=3+5*9
elif n[0]=='P':
  c+=2+3*9
elif n[0]=='Q':
  c+=2+4*9
elif n[0]=='R':
  c+=2+5*9
elif n[0]=='S':
  c+=2+6*9
elif n[0]=='T':
  c+=2+7*9
elif n[0]=='U':
  c+=2+8*9
elif n[0]=='V':
  c+=2+9*9
elif n[0]=='W':
  c+=3+2*9
elif n[0]=='X':
  c+=3+0*9
elif n[0]=='Y':
  c+=3+1*9
else:
  c+=3+3*9

c+=int(n[1])*8
c+=int(n[2])*7
c+=int(n[3])*6
c+=int(n[4])*5
c+=int(n[5])*4
c+=int(n[6])*3
c+=int(n[7])*2
c+=int(n[8])
c+=int(n[9])

if c%10==0:
  print("合法")
else:
  print("不合法")
  