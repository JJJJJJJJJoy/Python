num = int(input())    #輸入-第幾個數字(人類的索引值)
list = []           #一空清單，放數字

for i in range(num):
    if i == 0:      #如果i=0，num=0
        num = 0
        list = [0]
    elif i == 1:    #如果i=1, num=1
        num = 1
        list = [0, 1]    #清單為[0,1]
    else:                #如果i>1
        num = list[-1] + list[-2] #num=兩個數字相加
        list.append(num)          #將num加為第二個字
      
print(list[-1])