class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        finallist = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    finallist.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[i] + nums[l] +nums [r] >0:
                    r-=1
                elif nums[i] + nums[l] + nums [r] < 0:
                    l+=1
                
                
        
        return finallist


            