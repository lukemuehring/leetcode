class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longest = 0
        for n in numSet:
            if n-1 not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest



        #     else:
        #         currMaxSeq = 1
        #         ogNum = num
        #         while num+1 in hashSet:
        #             currMaxSeq += 1
        #             num += 1
                
        #         if currMaxSeq > result:
        #             result = currMaxSeq
        
        # return result