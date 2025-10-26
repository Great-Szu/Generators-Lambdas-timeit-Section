import timeit

argument = """\
gc.enable()
text = "what have the romans ever done for us"
"""


text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

# use map
map_capitals = list(map(str.upper, text))
print(map_capitals)

function1 = """\
words = [word.upper() for word in text.split(' ')]
"""

# use map
function2 = """\
map_words = list(map(str.upper, text.split(' ')))
"""

for x in map(str.upper, text):
    print(x)

result1 = timeit.timeit(function1, setup=argument, number=10000)
result2 = timeit.timeit(function2, setup=argument, number=10000)

print(result1)
print(result2)
