# разбиение числа на два
def partitioning_number(n):
    partitions_of_number = []
    for i in range(2, n // 2 + 1):
        partitions_of_number.append((i, n - i))
    return partitions_of_number


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


# проверка если ли один список в другом
def is_list_in_list(a, b):
    i = 0
    while i < len(a) and a[i] in b:
        i += 1
    if i == len(a):
        return True
    return False


def main():
    max_n = 10 ** 5
    prime_numbers = sieve_of_eratosthenes(max_n)
    success = True
    n = 4
    while success and n <= max_n:
        partitions_of_number = partitioning_number(n)
        index_of_partition = 0
        # проверка каждого разбиения
        while (index_of_partition < len(partitions_of_number) and
               not is_list_in_list(partitions_of_number[index_of_partition], prime_numbers)):
            index_of_partition += 1
        if index_of_partition == len(partitions_of_number):
            print(f"Число {n} нельзя разложить в виде 2-х простых чисел")
            success = False
        n += 2
    if success:
        print(f"Чётные числа до {max_n} можно разложить в виде 2-х простых чисел")


if __name__ == '__main__':
    main()
