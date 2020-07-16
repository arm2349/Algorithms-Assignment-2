import sys

def compute_min_refills(distance, tank, stops):
    #Constraints:
    assert distance>=1 and distance<=10**5 and tank>=1 and tank<=400
    for i in stops:
        assert i<i+1
    assert stops[-1]<distance and stops[0]>0
    #Edge case: total capacity of the tank is greater than the distance, so no refills needed
    if tank>distance:
        return 0
    #km: represents distance traveled so far, per tank
    km=0
    num_refills=0
    
    #add starting point of car's journey, represented by 0
    stops.insert(0,0)
    
    #add destination of car's journey, represented by the total distance
    stops.append(distance)

    for i in range(len(stops)-1):
        '''if distance from current to next stop is less than the tank's capacity,
        it is possible to travel that distance. Add that distance to km.'''
        if km + (stops[i+1]-stops[i]) <=tank:
            km+=(stops[i+1]-stops[i])
        # otherwise, it's impossible to travel that distance.
        else:
           #so, the tank must be refilled. 
            num_refills+=1
            '''reset km, and make it the distance from the current stop to the next.
             (without adding any previous accumulation of distance)'''
            km=(stops[i+1]-stops[i])
            '''If the distance to the next stop is greater than the capacity of the tank,
            then it is impossible to complete the journey.'''
            if km>tank:
                return -1
    return num_refills






if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
