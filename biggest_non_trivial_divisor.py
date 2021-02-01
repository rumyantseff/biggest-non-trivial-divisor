for n in range(2, 1000):
    is_prime = True
    for x in range(2, n):
        if n % x == 0:
            is_prime = False
            break
    if is_prime:
        nums = pow(n, 4)
        print(
            f'{nums}-------> biggest divisor: {pow(n, 3)}\n'
        ) if 123456789 <= nums < 223456789 else None
