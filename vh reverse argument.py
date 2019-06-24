
def reversed_args(f):
    def func(*args):
        args = list(args)
        n = len(args)
        new_args = []

        #reverse the function args using for loop
        for i in range(n):
            new_args.append(args[n-1])
            n -= 1
        return f(*new_args)
        
    return func
    

int_func_map = {
    'pow': pow,
    'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
}

string_func_map = {
    'join_with': lambda separator, *args: separator.join(args),
    'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
}

queries = int(input())
for _ in range(queries):
    line = input().split()
    func_name, args = line[0], line[1:]
    if func_name in int_func_map:
        args = list(map(int, args))
        print(reversed_args(int_func_map[func_name])(*args))
    else:
        print(reversed_args(string_func_map[func_name])(*args))
