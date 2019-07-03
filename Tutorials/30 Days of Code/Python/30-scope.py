class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        sorted_array = sorted(self.__elements)
        self.maximumDifference = abs(sorted_array[-1] - sorted_array[0])


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)