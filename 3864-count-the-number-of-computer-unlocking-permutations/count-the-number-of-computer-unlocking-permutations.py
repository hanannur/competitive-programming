class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        N = len(complexity)

        for i  in range(1,N):
            if complexity[0] >= complexity[i]:
                return 0

        ans = 1

        for i in range(1,N):
            ans *= i

        return ans%mod