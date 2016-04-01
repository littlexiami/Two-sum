class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target-x in dict:
                return [dict[target-x], i]
            dict[x] = i
    
# test cases
print 'Test Case 1'
test = Solution()
print test.twoSum([2,7,11,15],9)
print 'Expected: [0,1]'

print 'Test Case 2'
test = Solution()
print test.twoSum([2,7,11,15],13)
print 'Expected: [0,3]'

print 'TestCase 3'
test = Solution()
print test.twoSum([2,7,11,15],1)
print 'Expected: [-1]' # null case