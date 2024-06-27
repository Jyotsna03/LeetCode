class Solution:
    def isHappy(self, n: int) -> bool:
        def sqnum(n):
            sum=0
            while n>0:
                    rem=n%10
                    sum+=rem**2
                    n=n//10
            return sum
        
        for i in range(100):
            n = sqnum(n)
            if n==1:
                return True
        else:
            return False
        