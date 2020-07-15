
import sys

def max_dot_product(a, b):
    #list 'a' contains the profit-per-click
    #list 'b' contains the expected number of clicks per day
    #return dot product of a and b sorted from highest to lowest to obtain maximum revenue
    assert n>=1 and n<=1000
    for i in a:
        assert i>=(-10)**5
    for i in b:
        assert i<=10**5
    a.sort(reverse=True)
    b.sort(reverse=True)
    revenue = 0
    for i in range(len(a)):
        revenue += a[i] * b[i]
    return revenue

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
