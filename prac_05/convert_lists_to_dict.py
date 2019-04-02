names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

def convert_lists_to_dict(list_1, list_2):
    converted = list(zip(list_1, list_2))  # list of tuples
    converted = dict(zip(list_1, list_2))

    temp = {}
    for i, item in enumerate(list_1):  # Does not deal with different sized lists
        temp[list_1[i]] = list_2[i]
    return temp

print(convert_lists_to_dict(names, dates_of_birth))