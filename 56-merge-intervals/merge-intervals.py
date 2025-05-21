class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []

        if not intervals:
            return results
        
        if len(intervals) == 1:
            return intervals

        intervals.sort(key = lambda i : i[0])
        curr = intervals[0]

        for i in range(0, len(intervals)-1):
            # build the current interval
            nextI = intervals[i+1]


            # if curr interval's max is greater than or equal to interval B's min, we have a merge
            # the current intervals max = next intervals max.
            print(curr)
            print(nextI)
            if curr[1] >= nextI[0]:
                curr[1] = max(curr[1], nextI[1])
            else:
                results.append(curr)
                curr = nextI

            if i == len(intervals) - 2:
                results.append(curr)

        return results

        # if not: append current interval to results list
        # curr now equals interval B

        # return results

        '''
        intervals = [[1,3],[2,6],[8,10],[15,18]]

        curr interval [8, 10]
        results [[1,6], [8,10], 
        '''
        