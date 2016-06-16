__author__ = 'Apospraf'


def delchar(string):
    chars = ['!', '@', '#', '$', '%', '%', '^', '&', '*', "(", ")", "-", ",", ".", "?", ";", ":"]
    j = 0

    while j < len(chars):
        string = string.replace(chars[j], " ")
        j += 1

    return string
