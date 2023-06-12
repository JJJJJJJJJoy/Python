n=input()


if '+' in n: 
  l=n.split('+')
  print(int(l[0])+int(l[1]))
elif '-' in n:
  l=n.split('-')
  print(int(l[0])-int(l[1]))
elif '*' in n: 
  l=n.split('*')
  print(int(l[0])*int(l[1]))
elif '/' in n:
  l=n.split('/')
  print(int(int(l[0])/int(l[1])))

