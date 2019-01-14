"""
dynamic programming approach used
to calculate error as wrong way to go in rota
i am using a stopping place for the previous day
so error is minimum
151044012
ugurkan ATES
cse 321 algorithm and design analysis.
part1


"""


def optimalrota(hotels):
    rota = []
    error = []  # error margin hesaplamak icin
    for i in range(len(hotels)):
        error.insert(i,pow(200 - hotels[i], 2))
        rota.insert(i,0)
        for j in range(i):
            temp = error[j] + pow((200 - (hotels[i] - hotels[j])), 2)
            if temp < error[i]:
                error[i] = temp
                rota[i] = j + 1

    outputRota = []
    index = len(rota) - 1
    while index >= 0:
        outputRota.insert(0, index + 1)
        index = rota[index] - 1
    print("Penalties of this  = ", len(hotels)-1)
    print("OUTPUT rota  = ", outputRota)


A = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
# B = [20, 40, 60, 940, 1500]output 3,4,5
optimalrota(B)
