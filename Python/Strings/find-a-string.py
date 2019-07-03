def count_substring(string, sub_string):
    n1 = len(sub_string)
    n2 = len(string)
    n = n2 - n1 +1 
    parts = []
    for i in range(0,n):
        parts.append(string[i:i+n1])
    
    matchs = len(list(filter(lambda x: x == sub_string, parts)))

    return matchs
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, substring)
    print(count)