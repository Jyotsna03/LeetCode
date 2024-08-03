class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Compute the prefix XOR array in place
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        
        # Answer each query using the prefix XOR array
        return [
            arr[queries[i][1]] ^ (arr[queries[i][0] - 1] if queries[i][0] > 0 else 0)
            for i in range(len(queries))
        ]
