from medals_data import medals_table

options = {
    'C': ('country',),
    'G': ('gold medals',),
    'S': ('silver medals',),
    'B': ('bronze medals',),
    'R': ('rank',),
}

while True:
    for option, (description, *_) in options.items():
        print(f'{option}: Sort by {description}')
    print('Invalid choices will exit.')

    choice = input('Please select an option: ').upper()

    if choice == 'C':
        medals_table.sort(key=lambda d:d['country'])
    elif choice == 'G':
        medals_table.sort(key=lambda d:d['gold'], reverse=True)
    elif choice == 'S':
        medals_table.sort(key=lambda d:d['silver'], reverse=True)
    elif choice == 'B':
        medals_table.sort(key=lambda d:d['bronze'], reverse=True)
    elif choice == 'R':
        medals_table.sort(key=lambda d:d['rank'])
    else:
        break

    print(f'Sorted by {options[choice][0]}')
    for row in range(10):
        print(medals_table[row])
