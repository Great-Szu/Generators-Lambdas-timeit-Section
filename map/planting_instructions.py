from data import plants_list

# with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
#     for plant in plants_list:
#         # where_to_plant = 'window box' if plant.lifecycle == 'Perennial' else 'garden'
#         if plant.lifecycle == 'Perennial':
#             where_to_plant = 'window box'
#         else:
#             where_to_plant = 'garden'
#         print(f"{plant.name}: {where_to_plant}", file=output_file)


# def sort_perennials(item) -> str:
#     if item.lifecycle.casefold() == 'perennial':
#         return '1' + item.name
#     else:
#         return '0' + item.name


plants_list.sort(key=lambda x: '1' + x.name if x.lifecycle.casefold() == 'perennial' else '0' + x.name)

with open('planting_instructions.txt', 'w', encoding='utf-8') as output_file:
    for plant in plants_list:
        where_to_plant, who = ('window box', 'me') if plant.lifecycle == 'Perennial' else ('garden', 'gardener')

        # if plant.lifecycle == 'Perennial':
        #     where_to_plant = 'window box'
        #     who = 'me'
        # else:
        #     where_to_plant = 'garden'
        #     who = 'gardener'
        print(f"{plant.name}: {where_to_plant}, {who}", file=output_file)
