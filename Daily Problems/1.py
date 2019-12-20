# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


# Brute force O(N^2)
def two_sum(lst, k):
    for i in lst:
        for j in lst:
            if i != j and i + j == k:
                return True

    return False

# Using a seen set O(N)
def two_sum(lst, k):
    seen = []
    for num in lst:
        if k - num in seen:
            return True
        seen.append(num)
    return False
