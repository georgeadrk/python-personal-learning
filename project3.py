q: int = int(input('How many expenses today? '))
total: int = 0
i = 1
while i <= q:
    x: int = int(input(f'Expense {i}: '))
    total += x
    i += 1
avg: float = total / q

print(f'\nTotal spent: {total}')
print(f'Average spending: {avg}')