#Complexity of O(N)


class Solution(object):
    def maximumWealth(self, accounts):
        maximum_wealth = 0
        for account in accounts:
            wealth = sum(account)
            maximum_wealth = max(maximum_wealth,wealth)

        return maximum_wealth


#Complexity of (N*M)
def maximumWealth(self, accounts):
        wealth = 0
        for i in range(0,len(accounts)):
            sum = 0
            for j in range(0,len(accounts[i])):
                sum += accounts[i][j]
            wealth = max(wealth,sum)

        return wealth
