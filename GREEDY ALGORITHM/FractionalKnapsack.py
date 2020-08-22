class Items:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight

def fractional_knapsack(items,capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    value = 0
    for i in items:
        if(i.weight <= capacity):
            value += i.value
            capacity -= i.weight
        else:
            fraction = capacity/i.weight
            value += i.value*fraction
            capacity -= i.weight*fraction
    return value

n = int(input())
capacity = int(input())
weights = list(map(int,input().split(" ")))
values = list(map(int,input().split(" ")))
items = []
for i in range(n):
    items.append(Items(weights[i],values[i]))
print(fractional_knapsack(items,capacity))