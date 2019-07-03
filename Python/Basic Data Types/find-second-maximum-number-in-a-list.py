if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr_max = max(arr)
    filtered_list = list(filter(lambda x : x != arr_max, arr))
    print(filtered_list[-1])
