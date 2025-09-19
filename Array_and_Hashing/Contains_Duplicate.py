class Contains_Duplicate(object):
    def containsDuplicate(self, nums) -> bool: # -> (Expected return data type)
        # Code follows the same logic compared with their Java counterparts:
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False