class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1,len(arr)):
            arr[i] ^= arr[i-1]

        res = []
        for query in queries:
            start,end = query 
            if start > 0:
                xor_result = arr[end] ^ arr[start - 1]
            else:
                xor_result = arr[end]
            res.append(xor_result)
        return res                
        