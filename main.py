# Find a prime number by his index at the list
from math import sqrt


def index(n):
    count_idx = 0
    prime_num_lst = []
    gen = gen_prime_num()
    while count_idx <= n:
        prime_num_lst.append(gen.__next__())
        if count_idx == n:
            return prime_num_lst.pop(n)
        else:
            count_idx += 1


def gen_prime_num():
    res = 2
    while True:
        is_prime = True
        for x in range(2, int(sqrt(res) + 1)):
            if res % x == 0:
                is_prime = False
                break
        if is_prime:
            yield res
        res += 1


if __name__ == '__main__':
    print(index(4))
