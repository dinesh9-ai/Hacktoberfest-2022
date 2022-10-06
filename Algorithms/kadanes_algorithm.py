"""
This algorithm is used to find the largest sum in the given array in O(n) time complexity
"""
arr=[-1,3,0,6,9,1,-2,3]

max_sum=0
curr_sum=0
for i in arr:
    curr_sum += i
    max_sum=max(max_sum,curr_sum)
    if curr_sum<0:
        curr_sum=0
print(max_sum)