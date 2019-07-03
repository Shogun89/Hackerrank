#!/bin/python3

if __name__ == '__main__':
    n = int(input())

    remainder, repeat, max_repeat =0 , 0, 0
    while( n > 0):
        remainder = n % 2
        n = n//2
        if( remainder == 1):
            repeat += 1
            if ( repeat >= max_repeat):
                max_repeat = repeat
        else:
            repeat = 0

        
    print(max_repeat)


