import textwrap

def wrap(string, width):

    paragraph = textwrap.fill(string, width)
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
 
