def swap_case(s):
    
    def switch_case(s):

        if s.isupper():
            return s.lower()
        elif s.islower():
            return s.upper()
        else:
            return s
    result = ''.join(map(switch_case, s) )
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)