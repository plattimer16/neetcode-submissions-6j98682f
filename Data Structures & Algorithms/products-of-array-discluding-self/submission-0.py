class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        length = len(nums)
        right_product = [1]
        left_product = [1]
        rights = nums[::-1]
        for i in range(1, length):
            print(i)
            left_product.append(left_product[i-1] * nums[i-1])
            right_product.append(right_product[i-1] * rights[i-1])
        #print(right_product)
        right_product.reverse()
        products = [r * l for r, l in zip(right_product, left_product)]
        return products

        
        