from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any([len(x) == 0 for x in strs]):
            return ""
        prefix = ""
        try:
            for i in range(len(max(strs))):
                characters_to_compare = [item[0][i] for item in zip(list(x) for x in strs)]
                if all([item == characters_to_compare[-1] for item in characters_to_compare]):
                    prefix += characters_to_compare[-1]
                else:
                    break
        except:
            return prefix
        return prefix


print(Solution().longestCommonPrefix(
    ["flower", "flew", "flight"]
)) # FL
print(Solution().longestCommonPrefix(
    ["dog","racecar","car"]
)) # ""
print(Solution().longestCommonPrefix(
    ["helicopter", "helmet", "helium", "helper", "heliport"]
)) # hel
print(Solution().longestCommonPrefix(
    ['xenophobia', 'xenon', 'xenolith', 'xenotropic', 'xenotype']
)) # xeno
print(Solution().longestCommonPrefix(
    ["flower", "flower", "flower", "flower"]
)) # flower
print(Solution().longestCommonPrefix(
    ["","b"]
)) # ""
print(Solution().longestCommonPrefix(
    ["ab","a"]
)) # a
print(Solution().longestCommonPrefix(
    ["abby","abnormal", "ab"]
)) # ab