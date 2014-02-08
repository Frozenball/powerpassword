import json
import math


def get_chr(string, i, default=None):
    if i < 0 or i >= len(string):
        return default
    else:
        return string[i]

def triplet_generator(string):
    for i in range(-1, len(string)-1):
        yield (
            get_chr(string, i, '_SOL_'),
            get_chr(string, i+1),
            get_chr(string, i+2, '_EOL_')
        )


class PowerPassword(object):
    def __init__(self, chr_pairs):
        self.chr_pairs = chr_pairs
        self.total = sum(self.chr_pairs.values())

    def strength(self, password):
        score = 1.0
        for triplet in triplet_generator(password):
            triplet_score = self.chr_pairs.get(
                repr(triplet),
                1
            ) / float(self.total)
            score = score * triplet_score
        return -math.log(score)


if __name__ == '__main__':
    with open('builds/common_passwords.json') as infile:
        power_password = PowerPassword(json.loads(infile.read()))

        passwords = [
            '1234567890',
            '123456',
            'hello12345',
            'fl3qkfoae0',
            'qwerty',
            'helloworld',
            'redbanana',
            'yellowbanana',
            'iloveyou',
            'gjrk2r3ge',
            'hello123'
        ]
        for password in passwords:
            print "%s = %s" % (password, power_password.strength(password))