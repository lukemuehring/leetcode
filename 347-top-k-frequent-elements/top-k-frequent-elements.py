class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashM = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            if num in hashM:
                hashM[num] += 1
            else:
                hashM[num] = 1
        
        for num, count in hashM.items():
            freq[count].append(num)
        
        results = []
        i = len(freq) - 1
        while k > 0:
            currNums = freq[i]
            if len(currNums) > 0:
                for j in range(len(currNums)):
                    if k > 0:
                        results.append(currNums[j])
                        k -= 1
                    else:
                        break
            i -= 1
        return results