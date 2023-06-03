def missing_number(nums):
    # nums = [1, 2, 4, 5, 6,] --> suppose nums = 3 is missing number and range from 1 to 6 ( 6<=nums<=0 ) 
    length_nums = len(nums) + 1
    for i in range(length_nums):
        if i not in nums:
            return i
nums=[0,1, 2, 4]
missing_number(nums)

# most optimistic code 
def missing_number(nums):
    # nums = [1, 2, 4, 5, 6,] --> suppose nums = 3 is missing number and range from 1 to 6 ( 6<=nums<=0 ) 
    res1 = sum(nums)
    res2 = len(nums) * (len(nums) + 1) / 2
    return int(res1 - res2)
    #  In this we are using sume of number from 0 to n --> n(n+1)/2 and subract sum(nums) from that. 