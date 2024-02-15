"""
Algorithm: Knuth-Morris-Pratt (KMP)
Date created: February 15, 2024

Time Complexity: O(N+M)
Use Cases:
Pattern Matching: Particularly useful when you have to search for occurrences of a pattern within a text.
"""

class KMP:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def compute_lps(self):
        m = len(self.pattern)
        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if self.pattern[i] == self.pattern[length]:
                length+=1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

        return lps

    def search(self):
        n = len(self.text)
        m = len(self.pattern)
        lps = self.compute_lps()
        i = 0
        j = 0

        while i < n:
            if self.pattern[j] == self.text[i]:
                i += 1
                j += 1

            if j == m:
                print("Pattern found at index", i-j)
                j = lps[j-1]

            elif i < n and self.pattern[j] != self.text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

# Example usage:
kmp = KMP("AABAACAADAABAABA", "AABA")
kmp.search()