index_prefix = "RescueRanger909"
pet_list = {}
count = 0

def generate_key(index):
    return index_prefix+str(index)

def add_pet(index,breed,name):
    key = generate_key(index)
    pet_list[key] = (breed, name)
    global count
    count += 1

def remove_pet(index):
    key = generate_key(index)
    if key in pet_list:
        del pet_list[key]
        global count
        count -= 1

add_pet(468135, "shepherd", "Sharik")
add_pet(18343, "kolly", "Kolly")
add_pet(4843353, "british", "Wiskers")

remove_pet(18343)

print(pet_list)
print(count)