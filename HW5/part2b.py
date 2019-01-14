#151044012
# Algoritma odev 5 part 2
# cost of optimal plan

def opt(ny_list,sf_list,movingcost):

    opt_n = [0]
    opt_s = [0]
    i= 1 # for not getting array errors

    for i in range(len(ny_list)):
        opt_n.insert(i,ny_list[i] +min(opt_n[i-1],opt_s[i-1]+movingcost))
        opt_s.insert(i,sf_list[i] +min(opt_s[i-1],opt_n[i-1]+movingcost))

    #print(opt_n,opt_s)
    return min(opt_n[len(ny_list)-1],opt_s[len(ny_list)-1])



def main():
    movingcost = 10
    ny_list = [0,1,3,20,30]
    sf_list = [0,50,20,2,4]
    #a = 1

    a = opt(ny_list,sf_list,movingcost)
    print("returns the cost of an optimal plan ",a)
main()