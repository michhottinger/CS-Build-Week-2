class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        match = {}#create a dict to save i
        
        for i in range(len(nums)):
            missing_value = target - nums[i]
            
            if missing_value in match:
            #return the missing value with the matching index
                return match[missing_value], i
        
            match[nums[i]] = i#set current num to mapped index
