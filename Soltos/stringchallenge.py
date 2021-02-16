first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge

first_value.strip()
first_value.lower()
first_value.title()

# Second challenge

second_value.replace('-', '')
second_value.replace(' ','')

# Third challenge

third_value.replace('-', '')
third_value.replace(' ','')
third_value.swapcase()

print(first_value)
print(second_value)
print(third_value)

# Fourth challenge - use only the print() function (no f-strings)

print(fourth_value, fifth_value, sixth_value, sep='#', end='!\n')

# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.

print(f'{fourth_value} \n SUPERRR \n {fifth_value} \n {sixth_value:*^30}')