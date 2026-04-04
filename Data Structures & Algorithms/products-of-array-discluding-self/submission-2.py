class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = list()
        for i in range(0,len(nums)):
            leftProduct = 1
            rightProduct = 1
            for j in range(0,i):
                leftProduct *= nums[j]
            for j in range(i+1,len(nums)):
                rightProduct *= nums[j]
            output.append(leftProduct*rightProduct)
        return output
