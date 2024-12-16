# проверка разбиений числа
def check_partitions_of_number(n, prime_numbers):
    index_of_first_addend = 0
    success = False
    while prime_numbers[index_of_first_addend] <= n // 2 and not success:
        # проверка простые ли числа слагаемые
        if n - prime_numbers[index_of_first_addend] in prime_numbers:
            success = True
        index_of_first_addend += 1
    return success


# решето эратосфена
def sieve_of_eratosthenes(max_n):
    numbers = list(range(max_n + 1))
    prime_numbers = []
    for i in range(2, len(numbers)):
        if numbers[i] != 0:
            prime_numbers.append(i)
            for j in range(2 * i, len(numbers), i):
                numbers[j] = 0
    return prime_numbers


def main():
    max_n = 10 ** 5
    prime_numbers = sieve_of_eratosthenes(max_n)
    success = True
    n = 4
    while success and n <= max_n:
        # проверка разбиений числа
        if not check_partitions_of_number(n, prime_numbers):
            print(f"Число {n} нельзя разложить в виде 2-х простых чисел")
            success = False
        n += 2
    if success:
        print(f"Чётные числа до {max_n} можно разложить в виде 2-х простых чисел")


if __name__ == '__main__':
    main()
