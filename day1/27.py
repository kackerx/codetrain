def sol(nums, target):
    slow = -1
    fast = -1

    for i in range(len(nums)):
        if nums[i] == target:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[i]
            fast += 1

    print(nums, slow)


if __name__ == '__main__':
    sol([2, 3, 9, 2, 8, 7, 5, 2, 1, 2, 3, 2], 2)