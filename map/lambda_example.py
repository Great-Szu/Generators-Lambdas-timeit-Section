from medals_data import medals_table


def sort_key(d: dict) -> str:
    return d['rank']


medals_table.sort(key=sort_key)
print(medals_table)
