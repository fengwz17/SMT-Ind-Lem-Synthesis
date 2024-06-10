def ack(x, y):
    if (x == 0): return y + 1
    else:
        if (y == 0): return ack(x - 1, 1)
        else: return ack(x - 1, ack(x, y - 1))

for x in range(5):
    for y in range(5):
        print(x, y, ack(x, y))



