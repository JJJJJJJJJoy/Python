class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        count = 0          #變量用於存儲 digits 對應的數字
        j = 0              #變量用於表示十進制的位數
        for i in range(1, len(digits)+1):           #i變數在1到清單長度+1之間

            j = j*10                                       #十進位
            if j == 0:
                j = 1                                      #初始為1 
            count = count + digits[len(digits)-i]*j
        
        count = count + 1                           #清單+1

        print(count)
        digits = [int(i) for i in str(count)]       #轉換成字串

        return digits