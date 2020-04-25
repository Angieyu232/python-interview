'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Approach: bottom up constructing a dynamic table, dynamic programming

Solution: construct a table using dict

Time complexitu: size of coin list * amount, assume n means amount, O(n**2)
  On each step the algorithm finds the next F(i)F(i) in nn iterations, where 1\leq i \leq S1≤i≤S. Therefore in total the iterations are S*nS∗n.
Space complexity : O(S)O(S). We use extra space for the memoization table.

  金额从小到大，去掉一个硬币之后，剩下的余额可以选择 min (F(S-C0), F(S-C1), F(S-C3), ... )
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # calculate a dynamic program table, store the amount of coins needed for each target amount

        # initialize dp table with inf large number of size amount + 1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        #since the given coin denomination amount is unknow, no more init case
        # loop throgh each coin size
        for coin in coins:
            # loop through current coin size to target amount + 1
            for x in range(coin, amount + 1):
                # use 'amount + 1' cause range function is "[a, b) "
                dp[x] = min(dp[x], dp[x - coin] + 1)


        return dp[amount] if dp[amount] != float('inf') else -1

  #corner case, if there is no way to solve the change, returnn 0
    def coin_change2(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[amount]

