
#151044012 - UGURKAN ATES ALGORITHM 5 PART1
# Weight-Photocoppying problem
# very similiar to optimal data storage problem


#s. As we can always do this whenever the
#elements are not in a sorted order, and, starting at any sequence we can do
#this only finitely many times before arriving at a sorted order (by bubble sort),
#it shows that our solution is optimal.

def photo(jobs,weight):
    #for each jobs complettion time
    for i in  range(len(jobs)):
        print("%d's  jobs completionist TIME is = %d",i,calc(jobs,weight,i))

def calc(jobs,weight,i):
    sumar = 0
    for j in range(len(jobs)):
        if(i == j):
            sumar+=weight[j]*jobs[j]
        else:
            sumar+=weight[j]*sum(jobs)

    return sumar




def main():
    jobs = [1,3] # jobs complete time
    weight = [10,2]
    photo(jobs,weight)

main()