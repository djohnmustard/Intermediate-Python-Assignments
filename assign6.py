fib = [0, 1]
fib0 = 0
fib1 = 1
for x in range(1, 21):
    print(fib0, end=" ")
    y = fib0 + fib1
    fib0 = fib1
    fib1 = y
