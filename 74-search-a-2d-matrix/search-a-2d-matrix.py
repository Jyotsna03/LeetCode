class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp=[]
        for i in matrix:
            for j in i:
                temp.append(j)
        if target in temp:return True
        else:return False

        