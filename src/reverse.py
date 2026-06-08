def reverse(s: str) -> str:
    # solution: O(n^2) time complexity, O(n^2) space complexity
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

def reverse2(s: str) -> str:
    # solution: O(n) time complexity, O(n) space complexity
    chars = list(s)

    def helper(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        helper(left + 1, right - 1)

    helper(0, len(s) - 1)
    return "".join(chars)

if __name__ == "__main__":
    print(reverse("reversed"))