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
        if lst_of_summands[-1] != i:
            lst_of_summands.append(i)
            remainder-=i
            i+=1
            if (i*2)==remainder:
                lst_of_summands.append(remainder)
                remainder=0
                break
            #added conditions !=0 because 0 is in the list by default.
            while 0 < (remainder - (i)) <i:
                i+=1
    del lst_of_summands[0]






    return lst_of_summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
