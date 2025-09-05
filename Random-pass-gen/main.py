import math, random

ascii_letters, digits, punctuation = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "0123456789",
    "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
)
all_characters = ascii_letters + digits + punctuation
min_length = 8
max_length = 16
num_passwords = 10
passwords = set()
while len(passwords) < num_passwords:
    length = random.randint(min_length, max_length)
    password = [
        random.choice(ascii_letters),
        random.choice(digits),
        random.choice(punctuation),
    ] + [random.choice(all_characters) for _ in range(length - 3)]
    random.shuffle(password)
    passwords.add("".join(password))
for pwd in passwords:
    print(pwd)