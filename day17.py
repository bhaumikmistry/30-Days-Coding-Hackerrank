
#Write your code here
class Calculator():
    
    def power(self,x,y):
        self.x = x
        self.y = y
        if self.x<0 or self.y<0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(self.x,self.y)
    
myCalculator=Calculator()
T=int(raw_input())
for i in range(T):
    n,p = map(int, raw_input().split())
    try:
        ans=myCalculator.power(n,p)
        print ans
    except Exception,e:
        print e    
    