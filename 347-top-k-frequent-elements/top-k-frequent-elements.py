class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n in hashM:
                hashM[n] += 1
            else:
                hashM[n] = 1
        
        for num, count in hashM.items():
            freq[count].append(num)
        
        results = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                results.append(n)
                if len(results) == k:
                    return results

        # (my boof ass code to iterate through the top k elements)
        # i = len(freq) - 1
        # while k > 0:
        #     currNums = freq[i]
        #     if len(currNums) > 0:
        #         for j in range(len(currNums)):
        #             if k > 0:
        #                 results.append(currNums[j])
        #                 k -= 1
        #             else:
        #                 break
        #     i -= 1
        return results