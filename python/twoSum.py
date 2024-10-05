
class Solution(object):
    def twoSum(self, nums, target):
        prevMap = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index
        return None

solution = Solution()

# Kullanıcıdan bir liste al
nums = list(map(int, input("Enter an integer list (separated by commas): ").split(',')))

# Kullanıcıdan hedef toplamı al
target = int(input("Enter the target total: "))

result = solution.twoSum(nums, target)

if result is not None:
    print(f"Sum of the nums: {result}")
else:
    print("Not found .")
