class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return nums

        counts = [0] * 3
        for i in range(len(nums)):
            if nums[i] == 0:
                counts[0]+=1
            if nums[i] == 1:
                counts[1]+=1
            if nums[i] == 2:
                counts[2]+=1
        
        # print(counts)
        currIndex = 0
        for i in range(counts[0]):
            nums[currIndex] = 0
            currIndex+=1

        for i in range(counts[1]):
            nums[currIndex] = 1
            currIndex+=1

        for i in range(counts[2]):
            nums[currIndex] = 2
            currIndex +=1

