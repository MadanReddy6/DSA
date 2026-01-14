def threeSum(bums):
'''
works but time complexity O(n3)
TLE in leet code 
'''
ans = set()
        nums.sort()
        for i in range(len(nums)- 1):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            diff = 0 - nums[i]
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[j] + nums[k] == diff:
                       ans.add((nums[i],nums[j],nums[k]))
        return list(ans)