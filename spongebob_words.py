import random


def convert(s):
    # initialization of string to ""
    new = ""

    # traverse in the string
    for x in s:
        new += x

        # return string
    return new

def split(word):
    return [char for char in word]

def Spongebob_words(string1):
    string1 = split(string1)
    for i in range(0, len(string1)):
        random_num = random.randint(1, 2)
        if random_num == 1:
            string1[i] = string1[i].capitalize()
    string1 = convert(string1)
    return string1



the_string = str(input("Enter a string: "))
print(Spongebob_words(the_string))

