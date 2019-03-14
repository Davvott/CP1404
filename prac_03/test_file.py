MIN_LEN = 4
pw = input("Enter your password: ")

while len(pw)< MIN_LEN:
    print("Your password must be at least {}".format(MIN_LEN))
    pw = input("Enter your password: ")

print("*"*len(pw))
