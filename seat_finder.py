# use the current list of possible seats and the current code
# to further partition the set
def find_item_from_code(code, remaining_items, lower_code, upper_code):
    if len(remaining_items) == 1:
        return remaining_items[0]

    if code[0] == lower_code:
        new_items = remaining_items[:int((len(remaining_items)/2))]
    else:
        new_items = remaining_items[int(len(remaining_items)/2):]

    return find_item_from_code(code[1:], new_items, lower_code, upper_code)

def find_row_from_code(code):
    return find_item_from_code(code, generate_n_items(128), 'F', 'B')

def find_seat_from_code(code):
    return find_item_from_code(code, generate_n_items(8), 'L', 'R')

def find_seat_id_from_code(code):
    row = find_row_from_code(code[:7])
    column = find_seat_from_code(code[7:])
    return (row * 8) + column

# generate a list of 0 -> n -1
def generate_n_items(n):
    return [number for number in range(0,n)]
