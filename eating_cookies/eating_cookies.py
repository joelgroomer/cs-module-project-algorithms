'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache=[]):
    # Your code here
    # print(f'n = {n}')
    # base case
    if n == 0:
        return 1

    if n < 0:
        return 0

    # set up cache
    if len(cache) == 0:
        for _ in range(n+1):
            cache.append(0)
        print(f'cache length {len(cache)} for input {n}')

    # check cache
    # print(f'{n} / {len(cache)}')
    if cache[n] != 0:
        return cache[n]

    # make 3 recursive calls
    val = eating_cookies(n-1, cache) + eating_cookies(n-2,
                                                      cache) + eating_cookies(n-3, cache)
    cache[n] = val
    return val


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 2

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
