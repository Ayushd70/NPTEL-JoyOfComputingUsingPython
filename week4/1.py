"""
Input Format:

The first line contains a number made up of 0's and 1's.

Output Format:

Print 'YES' or 'NO' accordingly without quotes.

Example:

Input:

101

Output:
YES

"""

A = input()
ls = []
li = str(A)
for j in li:
    ls.append(int(j))
count_z = 0
count_o = 0
for k in ls:
    if(k==1):
        count_o += 1
    if(k==0):
        count_z += 1

if((count_o == 1) or (count_z == 1)):
    print("YES")

else:
    if((count_o == 0) or (count_z == 0)):
        print("NO")
    else:
        print("NO")
