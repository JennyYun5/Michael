import random, string

fields = string.ascii_letters + string.digits


def get_random_sample():
    a = ''.join(random.sample(fields, 5))
    return a


def get_nbr1(randomCount, nbr=1):
    count = 0
    for i in range(randomCount):
        count += 1
        a = '-'.join([get_random_sample() for j in range(nbr)])
        print(count)
        yield a


if __name__ == '__main__':
    for i in get_nbr1(200, 5):
        print(i)

