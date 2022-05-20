class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                 
        for List in nums:
            
            if (target - List) in nums:
                index = nums.index(List) 
                output = list.append(index)
            return output