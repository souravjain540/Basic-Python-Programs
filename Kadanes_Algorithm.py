# Python3 code to implement Kadane's Algortihm

def maxSubArraySum(a):

    max_so_far = float('-inf')
    max_ending_here = 0

    for i in range(len(a)):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


if __name__ == "__main__":
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArraySum(a))
