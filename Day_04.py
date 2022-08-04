import unittest


def two_contiguous_digits(pw):
    for i in range(len(pw) - 1):
        if pw[i] == pw[i+1]:
            return True
    return False

def increasing_digit_only(pw):
    for i in range(len(pw) - 1):
        if pw[i] > pw[i+1]:
            return False
    return True


def follows_the_rules(password):
    pw = str(password)
    if len(pw) != 6:
        return False
    if not two_contiguous_digits(pw):
        return False
    if not increasing_digit_only():
        return False
    return True

starting_value = 100
ending_value = 120

tally = 0
for x in range(starting_value, ending_value+1):
    if follows_the_rules(x):
        tally += 1

print(f'Follows the rule count: {tally}')

class TestPasswordValidation(unittest.TestProgram):
    def test_password_validation(self):
        self.assertTrue(follows_the_rules(100000))
        self.assertFalse(follows_the_rules(99999))
        self.assertTrue(follows_the_rules(101011))
        self.assertFalse(follows_the_rules(101010))

if __name__ == "__main__":
    unittest.main()
