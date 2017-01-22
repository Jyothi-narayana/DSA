class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]
        low = 0 
        high = len(nums) - 1
        while (low < high):
            mid = (low + high) / 2
            if (nums[mid] < nums[low]):
                if (nums[mid] < nums[mid-1]):
                    low = mid
                    high = mid
                else:
                    high = mid - 1
            elif (nums[mid] > nums[high]):
                low = mid + 1
            elif (nums[mid] == nums[low] and nums[low] == nums[high]):
                #duplicates
                #print nums[low:(high+1)]
                if (len(nums[low:(high+1)]) > 2):
                    #print nums[low:mid]
                    #print nums[mid:high]
                    return min(self.findMin(nums[low:mid]), self.findMin(nums[mid:high]))
                else:
                    return nums[low]
            else: 
                high = low
        return nums[low]