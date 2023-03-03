def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        r = 1/0.5
        odds = odds * r            # edit here to update the odds
    print(odds)

n = 3
flip(n)
