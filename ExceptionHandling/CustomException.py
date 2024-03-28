class InvalidAgeError(Exception):
    pass


def check_if_voter(age):
    try:
        if age < 18:
            raise InvalidAgeError
        else:
            print("Can vote")

    except InvalidAgeError:
        print("Cannot vote")


check_if_voter(9)
check_if_voter(20)