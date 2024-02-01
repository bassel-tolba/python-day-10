
def name(f_name, l_name):
    count = 0
    new_f_name = ""
    new_l_name = ""
    for char in f_name:
        count += 1
        if count == 1:
            char =  char.upper()
        else:
            char = char.lower()
        new_f_name += char
    

    count = 0
    for char in l_name:
        count += 1
        if count == 1:
            char = char.upper()
        else:
            char = char.lower()
        new_l_name += char
    print(new_f_name + " " + new_l_name)
name("aHmad", "moHaMMad")
