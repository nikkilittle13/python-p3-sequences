#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []

    if length == 0:
        print([])
        return

    if length == 1:
        print([0])
        return

    fib_sequence.append(0)
    fib_sequence.append(1)

    for _ in range(length - 2):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    print(fib_sequence)
    pass