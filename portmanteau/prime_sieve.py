# N以下の素数のリストを出力する
def prime_sieve(N):
    if N < 2:
        return []
    search_list = list(range(2, N + 1))
    prime_list = []
    while search_list[0] <= N ** 0.5:
        prime_list.append(search_list[0])
        tmp = search_list[0]
        search_list = [i for i in search_list if i % tmp != 0]
    prime_list.extend(search_list)
    return prime_list


N = int(input())
print(prime_sieve(N))
