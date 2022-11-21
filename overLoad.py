class something:
    def __init__(self, val):
        self.val = val
        
    def __add__(self,other):
        return self.val + other.val
    
obj1 = something(2)
obj2 = something(3)
print(obj1 + obj2)