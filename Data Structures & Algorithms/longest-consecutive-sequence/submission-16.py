class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        beforeafter = set(nums)
        longest = 0
 

     

        for i in beforeafter:
            if i-1 not in beforeafter:
                count = 0
                while i+count in beforeafter:
                    count+=1
                longest = max(count,longest)




        return longest

        
            

        
            