"""
Algorithm: Knuth-Morris-Pratt (KMP)
Date created: February 15, 2024

Time Complexity: O(N+M)
Use Cases:
1. String Matching: Z-function can be used for substring matching and pattern matching similar to KMP.
2. String Compression: The Z-function can be employed in compression algorithms to identify repeating patterns in a string.
3. Longest Prefix Matching: It can be used to efficiently find the longest common prefix between different strings.
"""

class ZFunction:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def compute_z_array(self):
        concat_string = self.pattern + "$" + self.text
        n = len(concat_string)
        z = [0] * n
        l, r = 0, 0

        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and concat_string[z[i]] == concat_string[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        return z

    def search(self):
        z_array = self.compute_z_array()
        m = len(self.pattern)
        n = len(self.text)

        for i in range(n):
            if z_array[i + m + 1] == m:
                print("Pattern found at index", i)

# Example usage:
zf = ZFunction("AABAACAADAABAABA", "AABA")
zf.search()