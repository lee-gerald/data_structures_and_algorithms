nums = [-3, 0, 3, 12, 41, 100]


def reverse_list(nums):
    start_index = 0
    end_index = len(nums) - 1

    while start_index < end_index:
        temp_start = nums[start_index]
        nums[start_index] = nums[end_index]
        nums[end_index] = temp_start
        start_index += 1
        end_index -= 1
    return nums

print(reverse_list(nums))


