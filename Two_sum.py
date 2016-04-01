class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp=nums
        num=sorted(nums)
        l=0
        r=len(nums)-1
        while l<r:
            if num[l]+num[r]<target:
                print num[l]
                l+=1
            elif num[l]+num[r]>target:
                print num[r]
                r-=1
            else:
                return [tmp.index(num[l]),tmp.index(num[r])]