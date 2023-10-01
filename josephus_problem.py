def josephusProblem(n, k):
    if n == 1:
        return 1
    else:
        return (josephusProblem(n - 1, k) + k - 1) % n + 1


n = int(input("Enter the number of people: "))
k = int(input("Enter the value of k (position of persons to be killed): "))

res = josephusProblem(n, k)
print("The safe position for the Josephus problem is: ", res)
