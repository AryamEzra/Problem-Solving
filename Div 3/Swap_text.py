def swap_case(s):
    text = ""
    for i in s:
        #isupper is a fucntion that returns true or false
        if i.isupper() == True:
            text += (i.lower())
        else:
            text += (i.upper())
    return text

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)