def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            upper_char = chr(ord(char) - 32)
        else:
            upper_char = char
        print("{}".format(upper_char), end="")
    print()
