import bisect
n,k = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
left = 0
right = k
diff = nums[right]-nums[left]
j = bisect.bisect_right(nums,diff)
print(diff if j==k else -1)



