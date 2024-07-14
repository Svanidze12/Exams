# #
# Unique In Order 
def unique_in_order(sequence):
    final = []
    preserving = None
    for char in sequence[0:]:
        if char != preserving:
            final.append(char)
            preserving = char
    return final
    