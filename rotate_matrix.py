class RotateMatrix:
    def __init__(self, nums: list[list[int]]):
        self.nums = nums

    def solution(self):
        n = len(self.nums)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                self.nums[i][j], self.nums[j][i] = (
                    self.nums[j][i],
                    self.nums[i][j]
                )

        # Reverse each row
        for row in self.nums:
            left = 0
            right = n - 1

            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

    def print_solution(self):
        for row in self.nums:
            print(*row)

nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = RotateMatrix(nums)
sol.solution()
sol.print_solution()