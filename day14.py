

class Difference:
    def __init__(self, a):
        self.__elements = a

#Add your code here
    def computeDifference(self):
        olddiff=0
        for i in self.__elements:
            for j in self.__elements:
               
                diff = abs(i-j)
                if abs(i-j) >= olddiff:
                    olddiff = diff
                    self.maximumDifference = diff

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference

               