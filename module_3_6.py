# Task "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(args):
    result = 0
    if isinstance(args, (list, tuple, set)):
        for i in args:
            result += calculate_structure_sum(i)
    elif isinstance(args, dict):
        for i in args.values():
            values = i
            result += i
        for i in args.keys():
            keys = i
            result += len(keys)
    elif type(args) == str:
        result += len(args)
    elif type(args) == int:
        result += args
    return result

summ = calculate_structure_sum(data_structure)
print(summ)
