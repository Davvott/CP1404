MIN_LEN = 4

def main():
    pw = get_password()
    print_password(pw)


def print_password(pw):
    """Print Password, from password"""
    print("*"*len(pw))
    # for i in range(len(pw)):
    #     print("*")


def get_password():
    """Get and validate user's password, loop until criteria met"""
    pw = input("Enter your password: ")
    while len(pw) < MIN_LEN:
        print("Your password must be at least {}".format(MIN_LEN))
        pw = input("Enter your password: ")
    return pw


main()
