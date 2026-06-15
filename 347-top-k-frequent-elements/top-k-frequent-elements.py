import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxHeap = []
        countSet = {}
        for num in nums:
            if num not in countSet:
                countSet[num] = 1
            else:
                countSet[num] += 1
        
        for key in countSet:
            heapq.heappush(maxHeap, (-countSet[key], key))
        
        result = []
        for n in range(k):
            result.append((heapq.heappop(maxHeap)[1]))

        return result
        