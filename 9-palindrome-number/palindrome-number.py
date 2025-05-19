class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)  # Convert integer to string

        stack = []
        half = len(x) // 2

        # Push first half onto stack
        for i in range(half):
            stack.append(x[i])

        # For odd-length numbers, skip the middle character
        if len(x) % 2 == 1:
            half += 1

        # Compare second half with reversed first half from stack
        for i in range(half, len(x)):
            if stack.pop() != x[i]:
                return False

        return True