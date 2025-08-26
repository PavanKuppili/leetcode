class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxArea, Mdia=0, 0
        for w, h in dimensions:
            dia=w*w+h*h
            if Mdia<dia:
                Mdia=dia
                maxArea=0
            if dia==Mdia:
                maxArea=max(maxArea, w*h)
        return maxArea
        