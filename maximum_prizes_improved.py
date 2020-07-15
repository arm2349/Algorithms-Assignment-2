import sys

def optimal_summands(n):
    lst_of_summands = [0]
    remainder=n

    i=1
    #exception:
    if n==2:
        lst_of_summands.append(2)
        del lst_of_summands[0]
        return lst_of_summands


    while remainder>0:
        #add i to the list, as long as it is not already in it. To check if i is in the list, it is only necessary to inspect the last element.
        if lst_of_summands[-1] != i:
            lst_of_summands.append(i)
            remainder-=i
            i+=1
            
            #if i+i equals the remainder, then you can no longer use i, since you would have to add it twice and our list of summands can only contain distinct integers.
            #this means that the remainder cannot be broken down any further, so just add the remainder itself to the list.
            if (i*2)==remainder:
                lst_of_summands.append(remainder)
                # "use up" the remainder, and break out of the cycle as there are no remainding summands to append to the list.
                remainder=0
                break
            while 0 < (remainder - (i)) <i:
                i+=1
    #remove 0 from the list, since we are going to print the length of the list in order to display the number of summands (0 is not a summand).
    del lst_of_summands[0]



    return lst_of_summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
