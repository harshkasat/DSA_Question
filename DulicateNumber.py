# we can't sort the arr nor use space
def DulicateNumber(nums):
    ref={}
    for i in nums:
        if i in ref:
            ref[i] += 1
        else:
            ref[i] = 1
    for  k, v in ref.items():
        if v > 1:
            return k
nums = [1,3,4,2,2]
print(DulicateNumber(nums))

# ``The code I'm writing is Floyd's Tortoise and Hare's Algorithm``
# Floyd's Tortoise and Hare Algorithm, also known as the Cycle Detection Algorithm,
#  is an algorithm used to detect cycles in a linked list or an array. It employs two pointers,
#  a slow pointer and a fast pointer, initially set to the same position. The slow pointer moves forward one element at a time,
#  while the fast pointer moves forward two elements at a time. By continuously advancing the pointers and comparing their positions,
#  the algorithm can determine if a cycle exists in the data structure. If there is a cycle,
#  the slow and fast pointers will eventually meet at the same element.
#  This algorithm has a time complexity of O(n) and is widely used in various applications that involve cycle detection.
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]  
        fast = nums[0]  

        # 龜兔賽跑
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast:
                break

        # 找到循環起點
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow 