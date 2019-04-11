
def add_memberwise(list_1, list_2):
    # Add each indice of list together
    added = list((zip(list_1, list_2)))
    summed = [sum(list(i)) for i in added]

    comp = [sum(list(element)) for element in zip(list_1, list_2)]
    return comp

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(add_memberwise(l1, l2))
