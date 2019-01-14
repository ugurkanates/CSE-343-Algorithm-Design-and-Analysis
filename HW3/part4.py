#part4
# A Divide and Conquer based program 

def maxCrossingSum(arrtwo, l, m, h) : 

    sm = 0; left_sum = -10000

    for i in range(m, l-1, -1) : 
        sm = sm + arrtwo[i] 
    
        if (sm > left_sum) : 
            left_sum = sm 
    sm = 0; right_sum = -1000
    for i in range(m + 1, h + 1) : 
        sm = sm + arrtwo[i] 

        if (sm > right_sum) : 
            right_sum = sm 
    return left_sum + right_sum; 
def maxSubArraySum(arrtwo, l, h) : 

    if (l == h) : 
        return arrtwo[l] 
    m = (l + h) // 2

    return max(maxSubArraySum(arrtwo, l, m), 
            maxSubArraySum(arrtwo, m+1, h), 
            maxCrossingSum(arrtwo, l, m, h)) 
        

arrtwo = [2, 3, 4, 5, 7] 
n = len(arrtwo) 

sume = maxSubArraySum(arrtwo, 0, n-1) 
print("sum is ", sume) 
