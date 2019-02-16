def first_non_repeating_char(string):
    for i in string:
        if len([x for x in string if x==i]) == 1:
            return i
        else:
            string.replace('i','')

print(first_non_repeating_char(input()))
