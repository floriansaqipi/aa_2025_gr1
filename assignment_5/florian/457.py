from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        visited = set()

        for i in range(n):
            if i in visited:
                continue

            direction = nums[i] > 0
            current_path = set()
            j = i

            while True:
                if (nums[j] > 0) != direction:
                    break

                next_j = next_index(j)

                if next_j == j:
                    break

                if next_j in current_path:
                    return True

                current_path.add(j)
                visited.add(j)
                j = next_j

        return False



if __name__ == "__main__":
    s = Solution()

    tests = [
        ([2, -1, 1, 2, 2], True),
        ([-1, -2, -3, -4, -5, 6], False),
        ([1, -1, 5, 1, 4], True),
        ([1, 2, 3, 4, 5], True),
        ([-2, 1, -1, -2, -2], False),
        ([1, 1, 1, 1, 1], True),
        ([-1, -1, -1, -1], True),
        ([3, 1, 2], True),
    ]

    for nums, expected in tests:
        result = s.circularArrayLoop(nums)
        print(f"nums = {nums} result = {result} expected = {expected}")
