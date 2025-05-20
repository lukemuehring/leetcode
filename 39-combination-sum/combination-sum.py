class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # decision tree where one side, we choose a number from candidates
        # the other side, we choose everything except candidates

        results = []

        def dfs(i: int, currList: List[int], currTarget: int):
            if i >= len(candidates) or currTarget < 0:
                return
            if currTarget == 0:
                results.append(currList.copy())
                return
            
            currVal = candidates[i]
            currList.append(currVal)
            dfs(i, currList, currTarget - currVal)

            currList.pop()
            dfs(i + 1, currList, currTarget)


            '''
            [2 3 5] target = 7

            [2] []
            [2,3] []
            '''





        dfs(0, [], target)
        return results
            
        