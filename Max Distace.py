class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        li = []
        for i, item in enumerate(A):
            li.append((item, i))
        
        li.start()

        max_gap = 0
        min_number = li[0][1]
        for i in range(1, len(li)):
            if li[i][1] < min_number:
                min_number = li[i][1]
            else:
                max_gap = max(max_gap, li[i][1] - min_number)
        
        return max_gap