def nextPermutation(nums):
    # Step 1: Find the rightmost position where nums[i] < nums[i + 1]
    i = len(nums) - 2

    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find the rightmost number greater than nums[i]
    if i >= 0:
        j = len(nums) - 1

        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Step 3: Swap them
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse everything after i
    nums[i + 1:] = reversed(nums[i + 1:])