"""
Print second maximum and second minimum separated by a space

Example:

Input:

1 2 3 4 5

Output:

4 2

"""

a = [int(x) for x in input().split()]

a.sort() #this command sorts the list in ascending order

print(a[-2],a[1])
