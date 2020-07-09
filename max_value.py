import sys

def get_optimal_value(capacity, weights, values):
    #Constraints
    assert n>=1 and n<=1000
    assert capacity>=0 and capacity<=2 * 10**6
    for i in values:
        assert i>=0 and i<=2 * 10**6
    for i in weights:
        assert i>0 and i<=2 * 10**6

    #Initializations
    value_per_kg=[]
    max_value=0
    for i in range(len(weights)):
        value_per_kg.append(values[i]/weights[i])

    largest_val=value_per_kg.index(max(value_per_kg))

    #Edge cases
    if values[largest_val]==0:
        max_value=0
        return max_value

    if sum(weights)<capacity:
        for i in values:
            max_value+=i
        return max_value

    #Main cases
    while weights[largest_val]<=capacity:
        max_value+=values[largest_val]
        capacity-=weights[largest_val]
        weights[largest_val]=0
        values[largest_val]=0
        value_per_kg[largest_val]=0
        largest_val=value_per_kg.index(max(value_per_kg))
        if capacity==0:
            break

    fractional_amount_to_add=value_per_kg[largest_val]*capacity
    max_value+=fractional_amount_to_add
    capacity=0

    return max_value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2*n + 2):2]

    weights = data[3:(2*n +2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
