if __name__ == '__main__':
    S = input()
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(map(method, S)))