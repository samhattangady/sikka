def deserialize(serial):
    value = ''
    for i in range(0, len(serial), 2):
        value = ''.join([serial[i:i+2], value])
    return value

def read_var_int(in_file):
    var_int = in_file.read(2)
    if var_int == 'fd':
        var_int = deserialize(in_file.read(2 * 2))
    elif var_int == 'fe':
        var_int = deserialize(in_file.read(3 * 2))
    elif var_int == 'ff':
        var_int = deserialize(in_file.read(4 * 2))
    return int(var_int, 16)