import time


def factorize_sync(*numbers):
    result = []
    for number in numbers:
        factors = [i for i in range(1, number + 1) if number % i == 0]
        result.append(factors)
    return result


start_time = time.time()
a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
end_time = time.time()


def test_factorize(factorize_func):
    a, b, c, d = factorize_func(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    print("Test passed!")


start_time_sync = time.time()
test_factorize(factorize_sync)
end_time_sync = time.time()
print("Synchronous execution time:", end_time_sync - start_time_sync, "seconds")
