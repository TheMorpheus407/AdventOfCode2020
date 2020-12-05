with open('five') as f:
    seats_original = f.readlines()

#seats_original = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
seats = []
for i in seats_original:
    i = i.replace('\n', '')
    row = int(i[:7].replace('F', '0').replace('B', '1'), 2)
    column = int(i[-3:].replace('L', '0').replace('R', '1'), 2)
    seat_id = row * 8 + column
    seats.append(seat_id)
seats = sorted(seats)
x = set(range(seats[0], seats[-1])) - set(seats)

print("our seat: ", list(x)[0])
print("maximum seat id:", max(seats))