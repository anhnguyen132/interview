# https://leetcode.com/problems/maximum-number-of-balloons/


def maxNumberOfBalloons(text: str) -> int:
    """
    Time O(n + 5) = O(n), Space O(5) = O(1)
    """
    d = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
    for c in text:
        if c in d:
            d[c] += 1

    minCount = float("inf")
    for c in d:
        if c in set(["b", "a", "n"]):
            minCount = min(minCount, d[c])
        else:
            minCount = min(minCount, d[c] // 2)

    return minCount


print(maxNumberOfBalloons("loonbalxballpoon") == 2)
print(maxNumberOfBalloons("nlaebolko") == 1)
print(maxNumberOfBalloons("leetcode") == 0)
