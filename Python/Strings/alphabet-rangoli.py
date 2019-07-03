import string
def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    rangoli1 = ['-'.join(alpha[size-1:i:-1]+ alpha[i:size]).center(width,'-') for i in range(size)[::-1] ]
    rangoli2 = ['-'.join(alpha[size-1:i:-1]+ alpha[i:size]).center(width,'-') for i in range(size) ]
    rangoli = rangoli1 + rangoli2[1:]

    #print('\n'.join(map(str,rangoli1)))
    #print('\n'.join(map(str, rangoli2[1:])))
    print('\n'.join(map(str, rangoli)))
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    
    