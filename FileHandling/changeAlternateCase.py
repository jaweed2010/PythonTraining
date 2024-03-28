def change_case(str):
    changed_str = ""
    for i in range(0, len(str)):
        if i % 2 == 0:
            changed_str += str[i].upper()
        else:
            changed_str += str[i]
    return changed_str


f1 = open("input_changeCase")
file_string = (f1.read())
print(change_case(file_string))
f1.close()
