class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ok = []
        _max = max(candies)
        for candy in candies:
            ok.append(True if candy+extraCandies >= _max else False)
        return ok