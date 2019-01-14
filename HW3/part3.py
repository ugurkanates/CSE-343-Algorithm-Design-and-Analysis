#part3 
def checkWhetever(array, index): 
    for i in range(index): 
        if array[i] is i: 
            return i 
    # if not found return -1
    return -1
  
array = [1,2,3,4,6,5] 
index = len(array) 
print("finding out = " + str(checkWhetever(array,index))) 
  
#o n time 