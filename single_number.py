# This can be done using Bitwise manipulations
def singleNumber(nums) -> int:
    sol = 0
    for i in nums:
        sol ^= i
        return sol
    
nums = [4,1,2,1,2]
print(singleNumber(nums))
# This can also be done by without bitwise manipulations

def singleNumber(nums) -> int:
    ref ={}
    for i in nums:
        if i in ref:
            ref[i] += 1
        else:
            ref[i] = 1
    for  k, v in ref.items():
        if v == 1:
            return k
nums = [4,1,2,1,2]
print(singleNumber(nums))