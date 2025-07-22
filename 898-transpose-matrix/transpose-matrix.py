class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed=[]
        for i in range(len(matrix[0])):
            edited=[]
            for j in range(len(matrix)):
                edited.append(matrix[j][i])
            transposed.append(edited)
        return transposed
            