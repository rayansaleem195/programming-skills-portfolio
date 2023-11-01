#Exercise 5: Pets

pets = []
#LIST IS NEEDED TO STORE DATA FROM THE DICT

pet = {
    'Animal':'malinois',
    'Pet Name':'Fido',
    'Owner Name':'John',
    'Food':'Meats, Cheese, Vegetables'}
pets.append(pet)


pet = {
    'Animal':'doberman',
    'Pet Name':'Floof',
    'Owner Name':'Don Eladio',
    'Food':'Cooked Chicken, Cooked Fish, Steamed Peas'}
pets.append(pet)

    
pet = {
    'Animal':'shark',
    'Pet Name':'lucy',
    'Owner Name':'white',
    'Food':'Fish Food'}
pets.append(pet)


for pet in pets:
    print("\nPet Info of",pet['Pet Name'].title()+":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
