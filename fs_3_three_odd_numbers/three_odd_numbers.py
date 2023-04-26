

def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    sum = nums[0]+nums[1]+nums[2]
    if sum % 2 == 1:
        return True

    for index in range(3, len(nums)):
        sum = nums[index-2] + nums[index-1] + nums[index]
        if sum % 2 == 1:
            return True
    return False
