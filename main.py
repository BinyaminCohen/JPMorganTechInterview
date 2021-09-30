# Find a prime number by his index at the list
import math


def index(n):
    count = 0
    prime_num_lst = []
    gen = gen_prime_num()
    while count <= n:
        prime_num_lst.append(gen.__next__())
        if (count == n):
            return prime_num_lst.pop(n)
        else:
            count += 1


def gen_prime_num():
    count = 2
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            yield count
        count += 1


if __name__ == '__main__':
    print(index(5))
