calls = 0

def count_calls():
    global calls
    calls +=1
    return calls

def string_info(string):
    tuple_str = (len(string), string.upper(), string.lower())
    count_calls()
    return tuple_str

def is_contains(string, list_):
    count_calls()
    return string.lower() in (item.lower() for item in list_)

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
