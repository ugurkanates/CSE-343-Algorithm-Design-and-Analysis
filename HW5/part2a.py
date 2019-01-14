# Algo Odev 5 part A
# 151044012 ugurkan ates
# show this algoritm not working
def notreturn_correct(ny_list,sf_list):
    i = 0
    for i in range(len(ny_list)):
        if ny_list[i] < sf_list[i]:
            print("NY in MONTH %d \n",i)
        else:
            print("SF in MONTH %d \n",i)




def main():
    ny_list = [1,3,20,30]
    sf_list = [50,20,2,4]
    notreturn_correct(ny_list,sf_list)
    print("its not same as SF, NY, SF, NY ")
main()