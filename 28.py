transformation = lambda x: x
values = [1, 23, 42, 'asdfg']
transformation_values = list(map(transformation,values))
if values == transformation_values:
    print('ok')
else:
    print('fail')