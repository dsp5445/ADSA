def sort(nums):

    for i in range(len(nums)):
        minposition = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minposition]:
                minposition = j


        temp = nums[i]
        nums[i] = nums[minposition]
        nums[minposition] = temp

    


nums = [8,2,100,2,4,55,5,0,5,21,5]
sort(nums)

print(nums)
