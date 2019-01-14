from array import array
"""
151044012 Ugurkan ates cse 321
besttimes kelime bolme odevi

"""


def splitStringIntoWords(dictonary, longestLength, stringToSplit):
    wordIndicator = array('i', [0]*len(stringToSplit))
    end = False
    wordIndicatorLength = len(wordIndicator)
    front = len(wordIndicator) -1
    back = 1
    while not end:
        if stringToSplit[front:front + back] in dictonary \
        and ((front + back) == wordIndicatorLength  \
        or wordIndicator[front+back] >= 1):
            wordIndicator[front] = back
            front = front - 1
            back = 1
        else:
            back = 1 + back
            if back >= longestLength or front + back > wordIndicatorLength:
                back = 1
                front = front - 1
        if front < 0:
            end = True
    if wordIndicator[0] > 0:
        return splitString(stringToSplit, wordIndicator)

    return "Not a valid phrase"

def splitString(stringToSplit, wordIndicator):
    wordIter = 0
    stringWithSpaces = ""
    while wordIter < len(stringToSplit):
        lengthOfword = wordIndicator[wordIter]
        stringWithSpaces += " "
        stringWithSpaces += stringToSplit[wordIter:wordIter + lengthOfword]
        wordIter += lengthOfword

    return stringWithSpaces





"""
Solution

We first need to describe our problem so let
d[i] = {
true if s[1 . . . i] is a valid sequence of words
f alse otherwise.
Then we want to determine d[n].
Now we need to describe our subproblems. s[1 . . . i] is a valid sequence of words if,
and only if, s[1 . . . j] is a valid sequence of words and s[j + 1 . . . i] is a valid word.
Thus d[i] is given by the following recurrence:
d[i] = {
f alse if i ≤ 0
max1≤j<i (d[j] ∧ dict(s[j + 1 . . . i])) otherwise.
To solve this recurrence efficiently we observe that d[i] depends only on values d[j]
where j < i. Thus we should solve d[1], d[2], . . . d[n]



"""
def main():


    dictonary = set()
    dictonary.add("it")
    dictonary.add("was")
    dictonary.add("the")
    dictonary.add("best")
    dictonary.add("of")
    dictonary.add("times")
    dictonary.add("tim")
    #dictonary.add("itwasthebestoftimes")
    """
    {"mobile","samsung","sam","sung", 
                            "man","mango","icecream","and", 
                             "go","i","like","ice","cream"}
    
    """
    dictonary.add("mobile")
    dictonary.add("samsung")
    dictonary.add("sam")
    dictonary.add("sung")
    dictonary.add("man")
    dictonary.add("mango")
    dictonary.add("icecream")
    dictonary.add("go")
    dictonary.add("i")
    dictonary.add("like")
    dictonary.add("ice")
    dictonary.add("cream")



    longestLength = len("icecream") #simdilik elle verem sonra dic dolas max bul ata gec tatava yapma# WAKE Up alalalla wake
    # shake up  ou wantod to i just wanna
    # why dount youkoutshakeup
    #selrifohussudicde
    #i cryyy whennn angel deserves to dieeeeeeeeeeeeeeeeeeeeeeeeeeee
    #eeeeeeeee
    #wake up
    #asdoasdıasd

    inputString = "itwasthebestoftimes"
    #another String to test hocam "ilikesamsung"
    #which will work and output !


    ## IT WORKS
    answer = splitStringIntoWords(dictonary,
                                 longestLength
                                 ,inputString)
    print(answer)

main()