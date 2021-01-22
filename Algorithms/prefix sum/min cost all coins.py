'''
@Author: rishi
https://www.geeksforgeeks.org/minimum-cost-for-acquiring-all-coins-with-k-extra-coins-allowed-with-every-coin/
'''

coin = [1, 2, 5, 10, 20, 50]
k = 3

ans = 0
coin.sort()
start = 0
end = len(coin) - 1

while start < end:
    ans += coin[start]
    start += 1
    end -= k

print(ans)
