class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(item.split(' ')) for item in sentences])