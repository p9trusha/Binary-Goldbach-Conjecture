import numpy
import time
from multiprocessing import Process, Manager
from sieve_of_atkin import sieve_of_atkin
from sieve_of_eratosthenes import sieve_of_eratosthenes
from sieve_of_sundaram import sieve_of_sundaram


max_n = 10 ** 5
global prime_numbers
global sieve
prime_numbers, sieve = sieve_of_eratosthenes(max_n)


# проверка разбиений числа
def check_partitions_of_number(n):
    if n == 4:
        return True
    index_of_first_addend = 0
    success = False
    while prime_numbers[index_of_first_addend] <= n // 2 and not success:
        # проверка простые ли числа слагаемые
        if sieve[(n - prime_numbers[index_of_first_addend]) // 2]:
            success = True
            # print(f"{n} = {prime_numbers[index_of_first_addend]} + {n - prime_numbers[index_of_first_addend]}")
        index_of_first_addend += 1
    return success


def check_partitions_of_number_in_segment(a, b, arr):
    for n in range(a, b + 2, 2):
        i = (n - 4) // 2
        arr[i] = check_partitions_of_number(n)


def main():
    max_n = 10 ** 5
    global prime_numbers
    global sieve
    prime_numbers, sieve = sieve_of_eratosthenes(max_n)

    start = time.time()
    processes = []
    number_of_processes = 8
    n_of_iterations = (4 + max_n) // 2 * ((max_n - 4) // 2 + 1)
    max_iters_in_p = n_of_iterations // number_of_processes + 1
    start_n = 4
    lst = Manager().list(range((max_n - 4) // 2 + 1))
    for i in range(number_of_processes):
        if i + 1 == number_of_processes:
            end_n = max_n
        else:
            end_n = int(-1 + (1 + 4 * max_iters_in_p + start_n ** 2 - 2 * start_n) ** 0.5) // 2 * 2
        process = Process(target=check_partitions_of_number_in_segment,
                          args=(start_n, end_n, lst))
        start_n = end_n + 2
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    print(time.time() - start)
    if all(lst):
        print(f"Все чётные числа до {max_n} можно разложить в виде 2-х простых чисел")
    else:
        print(f"Число {lst.index(False) * 2 + 4} нельзя разложить в виде 2-х простых чисел")


if __name__ == '__main__':
    main()
