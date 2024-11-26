def my_code(input_dict: dict, recursion_depth: int = 0):
    for dict_element in input_dict.items():
        if dict_element is not None:
            key = dict_element[0]
            value = dict_element[1]
            print(f"{recursion_depth * "\t"}{key}:")
            if type(value) == dict:
                my_code(input_dict=value, recursion_depth=recursion_depth+1)
            else:
                print(f"{(recursion_depth + 1) * "\t"}{value}")


print("\nCASE 1\n")
my_code({
    'first': 'first_value',
    'second': 'second_value'
})

print("\nCASE 2\n")
my_code({
    '1': {
        'child': '1/child/value'
    },
    '2': '2/value'
})