import sys

def largest_number(a):

    #constraints
    for i in a:
        assert int(i)>=1 and int(i)<=1000


    #input 'a' is a list of numbers (in string format)
    ordered_list=[]
    #ordered_list will become a sorted list(from greatest to smallest) of each input
    #which will later be joined as a string (then converted into an integer) to output the answer
    ordered_list.append(int(a[0]))
    del a[0]
    #take the first number from the list of inputs, as an arbitrary starting point for other numbers to compare against

    number=''

    #number will be formed from the contents of ordered_list, then converted into an integer which will be the resulting output

    def is_greater_or_equal(x,y):
        x=str(x)
        y=str(y)
        #convert to strings to enable access to each of their digits using indexing
        #obtain desired digits, then convert back to int when using comparison operators


        greater=None
        #greater becomes True if x is deemed to be greater than or equal to y, otherwise it becomes False.

        #cases involving zero
        if int(x)==0 and int(y)>0:
            return False
        if int(y)==0 and int(x)>0:
            return True


        #case 1: number of digits are equal
        if len(x)==len(y):
            i=0

            if int(x[0])>int(y[0]):
                greater=True
                #first digit of x is greater

            elif int(x[0])==int(y[0]):
                #first digits are equal: iterate with while loop until there is a tiebreaker
                while i<len(x):
                    if int(x[i])==int(y[i]):
                        #if tie remains unbroken through the end, x fulfills being >= to y.
                        greater=True
                        i+=1
                    elif int(x[i])>int(y[i]):
                        #broken tie: x is greater
                        greater=True
                        break
                    else:
                        #broken tie: y is greater
                        greater=False
                        break
            else:
                #first digit of y is greater
                greater=False

        #case 2: x is 1 digit, y is longer than 1 digit
        elif len(x)==1 and len(y)>1:

            if int(x)>int(y[0]):
                #x is greater than y's first digit
                greater=True
            elif int(x)==int(y[0]):
                #tie: look for tiebreaker
                j=0
                while j<len(y):
                    if int(x)==int(y[j]):
                        #tie remains unbroken, x fulfills being >= to y
                        j+=1
                        greater=True

                    elif int(x)>int(y[j]):
                        #broken tie: x is greater
                        greater=True
                        break
                    else:
                        #broken tie: y is greater
                        greater=False
                        break
            else:
                #x is less than y's first digit
                greater=False

        #case 3: y is 1 digit, x is longer than 1 digit
        elif len(y)==1 and len(x)>1:

            if int(y)>int(x[0]):
                #y is greater than x's first digit
                greater=False

            elif int(y)==int(x[0]):
                #tie: look for tiebreaker
                m=0
                while m<len(x):
                    if int(y)==int(x[m]):
                        #tie remains unbroken, x fulfills being >= to y
                        m+=1
                        greater=True
                    elif int(y)>int(x[m]):
                        #broken tie: y is greater
                        greater=False
                        break
                    else:
                        #broken tie: x is greater
                        greater=True
                        break

            else:
                #y is less than x's first digit
                greater=True

        #case 4: x is greater than 1 digit, but still has fewer digits than y
        elif len(x)>1 and len(x)<len(y):

            if int(x[0])>int(y[0]):
                #x's first digit is greater than y's first digit
                greater=True

            elif int(x[0])<int(y[0]):
                #x's first digit is less than y's first digit
                greater=False
            else:
                #tie: look for tiebreaker

                p=0
                while p<len(x):
                    if int(x[p])==int(y[p]):
                        #if tie remains unbroken until the end, check for more conditions. See below.
                        p+=1
                        greater=True
                    elif int(x[p])<int(y[p]):
                        #broken tie: x is less than y
                        greater=False
                        break
                    else:
                        #broken tie: x is greater than y
                        greater=True
                        break
                if p==len(x):
                    #Tie remained unbroken. Now, we check the following conditions:
                    if int(y[p])>int(x[0]):
                        #the digit of y in the position of 1 past x's final digit (example: x=23, y=234, so in this case 4)
                        #is greater than the first digit of x. This means x is less than y.
                        greater=False
                    elif int(y[p])<int(x[0]):
                        #the digit of y in the position of 1 past x's final digit (example: x=46, y=463)
                        #is less than the first digit of x. This means x is greater than y.
                        greater=True
                    else:
                        #the digit of y in the position of 1 past x's final digit (example: x= 54, y=545)
                        #is tied with the first digit of x. This means we must check for one final condition:
                        if int(y[p])>int(x[-1]):
                            #if this said digit of y is greater than the final digit of x, y is considered greater than x.
                            #example: x=54, y=545 --> y is greater.
                            greater=False
                        else:
                            #if this said digit of y is less than or equal to the final digit of x, y is considered less than x.
                            #example: (x=68, y=686) OR (x=55, y=555) --> x is greater.
                            greater=True


            #case 5: opposite of case 3. y has more than one digit, but fewer than x
            #same condition checks as the ones used in case 4.

        elif len(y)>1 and len(y)<len(x):
            if int(x[0])>int(y[0]):
                greater=True
            elif int(x[0])<int(y[0]):
                greater=False
            else:
                z=0
                while z<len(y):
                    if int(y[z])==int(x[z]):
                        greater=False
                        z+=1
                    elif int(y[z])>int(x[z]):
                        greater=False
                        break
                    else:
                        greater=True
                        break
                if z==len(y):
                    if int(x[z])>int(y[0]):
                        greater=True
                    elif int(x[z])<int(y[0]):
                        greater=False
                    else:
                        if int(x[z])<int(y[-1]):
                            greater=False
                        else:
                            greater=True

        return greater

    for i in range(len(a)):
        k=0
        #for each number in the list of inputs, check if this number is greater than the zeroeth element in the new, sorted list.
        #If it is greater, insert it into the zereoth position, and the former largest number will be shifted to the right.
        if is_greater_or_equal(int(a[i]), ordered_list[0])==True:
            ordered_list.insert(0, int(a[i]))

        else:

            while True:
                #print (int(a[i]), 'is being compared against', ordered_list[k])
                if is_greater_or_equal(int(a[i]), ordered_list[k])==False:
                    #look through the list until there is a larger number
                    #(or until you reach the end of the list)
                    k+=1
                    if k==len(ordered_list):
                        #break out of loop if you reach the end of the list
                        break
                else:
                    #break out of loop if you find a tiebreaker
                    break
            if k==len(ordered_list):
                #if you reached the end of the list, that means no number was larger.
                #which means, this number is the smallest, so just append it to the end of the sorted list.
                ordered_list.append(int(a[i]))
            else:
                #this means you found a greater number, so insert it at the position it belongs.
                #the smaller numbers will be shifted to the right.
                ordered_list.insert(k, int(a[i]))

    for i in range(len(ordered_list)):
        #since the sorted list required the use of integers, convert them back into strings so they can all be joined.
        ordered_list[i]=str(ordered_list[i])
    #assign the joined string to the variable 'number'.
    number=number.join(ordered_list)
    #return the output as an integer
    return int(number)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    assert int(data[0])>=1 and int(data[0])<=100
    a = data[1:]
    print(largest_number(a))
