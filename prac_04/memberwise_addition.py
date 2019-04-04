
def add_memberwise(list_1, list_2):
    # Add each indice of list together
    added = list((zip(list_1, list_2)))
    summed = [sum(list(i)) for i in added]

    comp = [sum(list(element)) for element in zip(list_1, list_2)]
    return comp

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(add_memberwise(l1, l2))
AliceBlue		#f0f8ff,
AntiqueWhite		#faebd7,
AntiqueWhite1		#ffefdb,
AntiqueWhite2		#eedfcc,
AntiqueWhite3		#cdc0b0,
AntiqueWhite4		#8b8378,
aquamarine1		#7fffd4,
aquamarine2		#76eec6,
aquamarine4		#458b74,
azure1		#f0ffff,
azure2		#e0eeee,
azure3		#c1cdcd,
azure4		#838b8b,
beige		#f5f5dc,
bisque1		#ffe4c4,
bisque2		#eed5b7,