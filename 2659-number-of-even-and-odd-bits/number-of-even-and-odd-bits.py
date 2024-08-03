class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        val = bin(n)[2::][::-1]
        l = [0 , 0]
        for i in range(0 , len(val)):
            if val[i]=='1':
                if i%2:l[1]+=1
                else:l[0]+=1
        return l
        
        