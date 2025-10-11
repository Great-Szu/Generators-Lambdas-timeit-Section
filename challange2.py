# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.

# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimeters.

# Our dimensions will be represented by a tuple, for the length, width and height.

# There are 2.54 centimetres to 1 inch

inch_measurement = (3, 8 , 20)

cm_measurement = tuple(x * 2.54 for x in inch_measurement)
print(cm_measurement, type(cm_measurement))

# Once you've got the correct values, change the code to produce a tuple, rather than a list.
