class Solution:
    def isHappy(self, n: int) -> bool:
        def sqnum(n):
            sum=0
            while n>0:
                    rem=n%10
                    sum+=rem**2
                    n=n//10
            return sum
        slow = n
        fast = sqnum(n)

        # Use two pointers to detect cycles
        while fast != 1 and slow != fast:
            slow = sqnum(slow)               # Move slow by 1 step
            fast = sqnum(sqnum(fast))        # Move fast by 2 steps

        return fast == 1  # If fast reaches 1, the number is happy
        