def split_and_join(line):
    split_case = line.split(" ")
    rejoin = "-".join(map(str, split_case))
    return rejoin

if __name__ == '__main__':