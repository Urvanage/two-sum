def twoSum(nums, target):
    b = list()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target :
                b.append(i)
                b.append(j)
                return b

