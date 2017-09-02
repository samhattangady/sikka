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
