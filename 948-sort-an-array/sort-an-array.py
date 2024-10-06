class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Use merge sort for guaranteed O(n log n) performance
        if len(nums) > 1:
            self.mergesort(nums, 0, len(nums) - 1)
        return nums

    def mergesort(self, nums, left, right):
        if left < right:
            mid = (left + right) // 2
            self.mergesort(nums, left, mid)
            self.mergesort(nums, mid + 1, right)
            self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        # Create temporary arrays to hold the two halves
        left_half = nums[left:mid + 1]
        right_half = nums[mid + 1:right + 1]

        # Indices for left, right, and merged array
        i, j, k = 0, 0, left

        # Merge the temp arrays back into nums
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
