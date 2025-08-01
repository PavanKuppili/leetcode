class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[[1]]
        for i in range(numRows-1):
            n=[1]
            for j in range(i):
                n.append(l[i][j]+l[i][j+1])
            n.append(1)
            l.append(n)
        return l