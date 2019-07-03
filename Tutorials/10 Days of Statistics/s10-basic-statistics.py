# Enter your code here. Read input from STDIN. Print output to STDOUT
import operator
def find_mean(nums):
    mean = 0
    for num in nums:
        mean += num
    mean = mean/len(nums)

    return mean

def find_median(nums):
    median = 0

    sorted_nums = sorted(nums)
    my_len = len(sorted_nums)

    if my_len % 2 ==0:
        median = (sorted_nums[my_len//2]+sorted_nums[my_len//2 -1])/2
    else:
        median = sorted_nums[my_len//2]

    return median
def find_mode(nums):
    freq_dict = {}
    mode = None
    for num in nums:
        if num in freq_dict:
            freq_dict[num] +=1
        else:
            freq_dict[num] = 1
        if ( mode is None) or (freq_dict[num] > freq_dict[mode]):
            mode = num
        elif (freq_dict[num] == freq_dict[mode]) and (num < mode):
            mode = num
    return mode



n = int(input())
my_input = [int(item) for item in input().split()]
print(find_mean(my_input))
print(find_median(my_input))
print(find_mode(my_input))
