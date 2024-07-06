class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Custom comparator function
        def compare(x, y):
            # Compare two numbers by concatenating them in both possible orders
            if x + y > y + x:
                return -1
            else:
                return 1

        # Convert all numbers to strings for comparison
        nums_str = list(map(str, nums))

        # Sort numbers using the custom comparator
        nums_str.sort(key=lambda x: x*10, reverse=True)

        # Join the sorted numbers into a single string
        largest_num = ''.join(nums_str)

        # Handle the edge case where the largest number is '0'
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num