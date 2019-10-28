
import math
import random



def majorityPair(set, m):
    newSet = []
    found = False
    firstFound = False
    K = math.floor(len(set)/3)+1
    for i in range(0,m):
        if firstFound == False:
            xr = random.choice(set)
            print("CHOSEN xr:", xr)
            count = 0
            for j in set:
                if j == xr:
                    count = count + 1
                    if count == K:
                        print("count == K")
                        for k in range(0,len(set)):
                            print("POPPING ELEMENT ...")
                            if set[k] != xr:
                                newSet.append(set[k])
                                print("Element popped, newSet:")
                                print(newSet)
                                if k == len(set)-1:
                                    firstFound = True
        if len(newSet) != 0:
            xt = random.choice(newSet)
            print("CHOSEN xt:", xt)
            count = 0
            for j in newSet:
                if j == xt:
                    count = count + 1
            if count == K:
                print(xt, "HAS K(", count, ") occurences in ", set, ", and so does ", xr)
                print("MAJORITY PAIR detected: (",xr,",",xt,")")
                found = True
    return found



if __name__ == "__main__":
    S = [2,2,1,5,1,9,2,1]
    print("LKENGTGBH :", len(S))
    print(majorityPair(S, 10))
