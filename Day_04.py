import unittest


def two_contiguous_digits(pw):
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1]:
            return True
    return False

def two_isolated_contiguous_digits(pw):
    repeat_count = 0
    i = 0
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1]:
            if (i == 0 or pw[i-1] != pw[i]) and (i == len(pw) - 2 or pw[i+2] != pw[i+1]):
                return True
    return False


def increasing_digit_only(pw):
    for i in range(len(pw) - 1):
        if pw[i] > pw[i+1]:
            return False
    return True


def follows_the_rules_part_1(password):
    pw = str(password)
    if len(pw) != 6:
        return False
    if not two_contiguous_digits(pw):
        return False
    if not increasing_digit_only(pw):
        return False
    return True

def follows_the_rules_part_2(password):
    pw = str(password)
    if len(pw) != 6:
        return False
    if not two_isolated_contiguous_digits(pw):
        return False
    if not increasing_digit_only(pw):
        return False
    return True


def tally_valid_passwords_part_1(start, end):
    tally = 0
    for n in range(start, end + 1):
        if follows_the_rules_part_1(n):
            tally += 1
    print(f'Follows the rule count: {tally}')
    return tally


def tally_valid_passwords_part_2(start, end):
    tally = 0
    for n in range(start, end + 1):
        if follows_the_rules_part_2(n):
            tally += 1
    print(f'Follows the rule count part 2: {tally}')
    return tally


class TestPasswordValidation(unittest.TestCase):
    def test_password_validation(self):
        self.assertFalse(follows_the_rules_part_1(99999))
        self.assertFalse(follows_the_rules_part_1(101011))
        self.assertFalse(follows_the_rules_part_1(101010))
        self.assertTrue(follows_the_rules_part_1(123378))

        self.assertFalse(follows_the_rules_part_2(123444))
        self.assertTrue(follows_the_rules_part_2(113444))

        self.assertTrue(follows_the_rules_part_2(112233))
        self.assertFalse(follows_the_rules_part_2(123444))
        self.assertTrue(follows_the_rules_part_2(111122))
        self.assertTrue(follows_the_rules_part_2(223333))
        self.assertFalse(follows_the_rules_part_2(555555))
        self.assertTrue(follows_the_rules_part_2(556777))



starting_value, ending_value = 172930, 683082
tally_valid_passwords_part_2(starting_value, ending_value)


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()
