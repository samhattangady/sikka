def deserialize(serial):
    """
    Deserialize or convert endianness.
    A lot of data in the block is stored in a serialized manner,
    specifically, the bytes are stored backwards. This function
    corrects that. Note that it reverses characters in pairs because
    one byte has 2 hex values.
    """
    value = ''
    for i in range(0, len(serial), 2):
        value = ''.join([serial[i:i+2], value])
    return value

def read_var_int(in_file):
    """
    var_int is a space saving data type
    The first byte defines how many bytes of data the var_int is taking
    If the value of the first byte is less than fd, then that is the
    value of the integer. If it is fd, then the next two bytes contain
    the integer value. For fe, next three bytes, and for ff, next four.
    """
    var_int = in_file.read(2)
    if var_int == 'fd':
        var_int = deserialize(in_file.read(2 * 2))
    elif var_int == 'fe':
        var_int = deserialize(in_file.read(3 * 2))
    elif var_int == 'ff':
        var_int = deserialize(in_file.read(4 * 2))
    return int(var_int, 16)