if __name__ == '__main__':
    n = int(input())
    print('\n'.join(["{num} x {iter} = {prod}".format(num=n , iter =i, prod= n*i) for i in range(1,11)]))