"""
Print the resultant array elements separated by a space. (no space after the last element)

Example:

Input:
4
2 5 3 1

Output:
3 8 8 3

"""
N = int(input())
A = [int(i) for i in input().split(" ")]
B = []
for i in range(len(A)-1, -1,-1):
    B.append(A[i])
C = []
for i in range(len(B)):
    C.append(A[i]+B[i])
for i in range(len(C)):
    if(i==len(C)-1):
        print(C[i])
    else:
        print(C[i],end=" ")
