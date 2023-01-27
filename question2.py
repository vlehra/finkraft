# Implement a Python function that takes a list of integers and a target number as input, and returns a tuple of two integers that add up to the target number.

class func:  
    def __init__(self, list1, target):  
        self.list1 = list1  
        self.target = target  
          
    def solution(self):  
        length = len(list1)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if list1[i]+list1[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)  
        return -1
        
list1 = [1, 2, 4, 5, 11]  
target = 13  
obj = func(list1, target)  
print(obj.solution())  