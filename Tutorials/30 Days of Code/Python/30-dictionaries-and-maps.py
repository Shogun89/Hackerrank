my_dict = {}

num = int(input())

for i in range(num):

    dict_entry =input().split()
    my_dict[dict_entry[0]] = dict_entry[1]

for i in range(num):
    query = input()
    if query in my_dict:
        print(query +"="+my_dict[query])
    else: 
        print("Not found")