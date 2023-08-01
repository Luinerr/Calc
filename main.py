my_st = input()

compiled_str = compile(my_st, 'string', 'eval')

print(eval(compiled_str))
