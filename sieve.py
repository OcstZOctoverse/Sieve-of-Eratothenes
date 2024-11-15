def is_divisible(integer, divisor):
    return integer % divisor == 0


def check_for_prime(number_str):
    number = int(number_str)
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if is_divisible(number, i):
            return False
    return True


def find_primes(limit, starting_number):
    primes = []
    current_number = starting_number
    while len(primes) < limit:
        if check_for_prime(str(current_number)):
            primes.append(current_number)
        current_number += 1
    return primes


usr_input_1 = int(input("What should the starting number be? ").strip())
usr_input_2 = int(input("How many numbers do you want? ").strip())
sieve = find_primes(usr_input_2, usr_input_1)
print(sieve)
