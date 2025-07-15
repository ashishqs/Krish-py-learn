def get_full_name(fn, ln):
    full_name = f"{fn} {ln}"
    
    return full_name
    
def get_full_name2(fn, ln):
    full_name = f"{ln}, {fn}"
    
    return full_name

def pad_me(name):
    return name.rjust(15, '0')
    
def pad_me2(name, length):
    while len(name) < length:
        name = "0" + name
    
    return name



print(f'"{get_full_name2("Shit", "FORLIFE")}"')

print(get_full_name("-Krish", "D"))

print(pad_me("Krish")) # should print 0000000000Krish
print(pad_me("Ashish")) # should print 000000000Ashish
print(pad_me2("Ashish", 20)) # should print 000000000Ashish



