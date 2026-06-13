class Solution:
    def removeDuplicates(self, s: str) -> str:
        cleaned = []
        for i in range(len(s)):
            if cleaned:
                top = len(cleaned) - 1
                if cleaned[top] == s[i]:
                    cleaned.pop()
                else:
                    cleaned.append(s[i])
            else:
                cleaned.append(s[i])
        return "".join(cleaned)

        