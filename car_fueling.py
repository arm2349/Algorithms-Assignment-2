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
    km=0
    num_refills=0
    stops.insert(0,0)
    stops.append(distance)

    for i in range(len(stops)-1):
        if km + (stops[i+1]-stops[i]) <=tank:
            km+=(stops[i+1]-stops[i])
        else:
            num_refills+=1
            km=(stops[i+1]-stops[i])
            #If the distance to the next stop is greater than the capacity of the tank
            if km>tank:
                return -1
    return num_refills






if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
