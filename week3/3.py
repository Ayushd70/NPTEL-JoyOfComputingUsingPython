"""
Print the numbers in a single line separated by a space which are not multiples of 5.

Example:

Input:

1 2 3 4 5 6 5

Output:

1 2 3 4 6

"""

a = [int(x) for x in input().split()]

b = []

for i in a:
    if(i%5!=0):
        b.append(i)

for i in range(len(b)):
    if(i==len(b)-1):
        print(b[i],end="")
    else:
        print(b[i],end=" ")
