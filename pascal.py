def get_row(row_index):
    row = [0] * (row_index + 1)
    row[0] = 1

    for current_row_number in range(1, row_index + 1):
        for position_in_row in range(current_row_number, 0, -1):
            row[position_in_row] = row[position_in_row] + row[position_in_row - 1]

    return row
# Пример
print(get_row(0))
print(get_row(1))
print(get_row(2))
print(get_row(3))
print(get_row(4))  
