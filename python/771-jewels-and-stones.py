class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
      return len([x for x in stones if x in jewels])