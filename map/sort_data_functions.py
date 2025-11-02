from medals_data import medals_table


def sort_country(d: dict) -> str:
    return d['country']


def sort_gold(d: dict) -> str:
    return d['gold']


def sort_silver(d: dict) -> str:
    return d['silver']


def sort_bronze(d: dict) -> str:
    return d['bronze']


def sort_rank(d: dict) -> str:
    return d['rank']


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
        medals_table.sort(key=sort_country)
    elif choice == 'G':
        medals_table.sort(key=sort_gold, reverse=True)
    elif choice == 'S':
        medals_table.sort(key=sort_silver, reverse=True)
    elif choice == 'B':
        medals_table.sort(key=sort_bronze, reverse=True)
    elif choice == 'R':
        medals_table.sort(key=sort_rank)
    else:
        break

    print(f'Sorted by {options[choice][0]}')
    for row in range(10):
        print(medals_table[row])
