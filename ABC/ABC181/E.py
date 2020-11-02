import bisect

n, m = map(int, input().split())
n = (n + 1) // 2
(*h_list,) = map(int, input().split())
(*w_list,) = map(int, input().split())
h_list.sort()
left, right = [0] * n, [0] * n
for i in range(n - 1):
    left[i + 1] = left[i] + h_list[2 * i + 1] - h_list[2 * i]
    right[i + 1] = right[i] + h_list[-(2 * i + 1)] - h_list[-(2 * i + 2)]
right.reverse()
ans = 10 ** 20
for w in w_list:
    i = bisect.bisect_left(h_list, w) // 2
    ans = min(ans, left[i] + abs(h_list[2 * i] - w) + right[i])
print(ans)
