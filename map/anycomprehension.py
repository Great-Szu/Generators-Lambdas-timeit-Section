from xml.dom.minidom import ProcessingInstruction

from data import people, plants_list, plants_dict

# people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")


if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("There is at least one grass type")
else:
    print("There is no grass")

print()
print("*" * 30, "CHALLENGE BELLOW", "*" * 30)
print()

# test = list(plants_dict.values())
# test2 = plants_dict.get(test[1])
# print(test)

challenge = any([plant.plant_type == "Grass" for plant in plants_dict.values()])

if challenge:
    print("Yep")
else:
    print("Nope")
narrowed_list = [name for name, details in plants_dict.items() if details.plant_type == "Grass"]
print(narrowed_list)

# challenge2 = [name for name in list(narrowed_list)]
# print(challenge2)
