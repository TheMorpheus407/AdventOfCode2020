import itertools
adjacent = [(i, j) for i, j in itertools.product(range(-1, 2, 1), repeat=2) if i != 0 or j != 0]

def count_adjacent_seats(row_id, col_id, seats):
    counter = 0
    for off_i, off_j in adjacent:
        if 0 <= row_id + off_i < len(seats) and 0 <= col_id + off_j < len(seats[row_id + off_i]) and seats[row_id+off_i][col_id+off_j] == "#":
            counter += 1
    return counter


def count_seeable_seats(row_id, col_id, seats):
    counter = 0
    for off_i, off_j in adjacent:
        row_idx = row_id + off_i
        col_idx = col_id + off_j
        while 0 <= row_idx < len(seats) and 0 <= col_idx < len(seats[row_idx]):
            if seats[row_idx][col_idx] == "#":
                counter += 1
                break
            if seats[row_idx][col_idx] == "L":
                break
            row_idx += off_i
            col_idx += off_j
    return counter


def simulate(seats, tolerance=4, on_sight=False):
    previous = []
    while previous != seats:
        previous = seats[:]
        seats = []
        for row_id, row in enumerate(previous):
            new_row = ""
            for col_id, col in enumerate(row):
                if not on_sight:
                    neighbors = count_adjacent_seats(row_id, col_id, previous)
                else:
                    neighbors = count_seeable_seats(row_id, col_id, previous)
                if col == ".":
                    new_row += col
                elif col == "L":
                    if neighbors == 0:
                        new_row += "#"
                    else:
                        new_row += "L"
                elif col == "#":
                    if neighbors >= tolerance:
                        new_row += "L"
                    else:
                        new_row += "#"
                else:
                    new_row += col
            seats.append(new_row)
        assert len(previous) == len(seats)
        assert len(previous[0]) == len(seats[0])
    return previous

def count_seated(seats):
    return list(itertools.chain(*seats)).count('#')


with open("11.txt") as f:
    seats = f.read().splitlines()
waiting_room = simulate(seats)
print(count_seated(waiting_room))

with open("11.txt") as f:
    seats = f.read().splitlines()
waiting_room = simulate(seats, tolerance=5, on_sight=True)
print(count_seated(waiting_room))