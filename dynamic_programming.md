# Dynamic Programming

### Leetcode problem - Coin Change 322

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.


### Assumption

Assume you have infinite amount of coins








## Approach 1
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Need an assumption, there is unlimited amount of coin denomination

        #need recursion to solve a N-Tree traversal question
        # to find the minimal coins needed, start traversal from larger coin denominations

        # F(S) = F(S-C) + 1
        # Take Care of corner cases, each path/traversal for finding the target sum need to save a count of coins





        def dp(n):
            if n == 0:
                return 0
            if n < 0 or not coins:
                return -1

            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                # 子问题无解，跳过
                if subproblem == -1: continue

                res = min(res, 1 + subproblem)
            return res if res != float('INF') else -1


        return dp(amount)
```



## Approach 2
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

     # construct a table of
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```

Other solution similar to backtracking:

```python
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')] * amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float('inf') else -1
```



