"""
Algorithm: Rabin-Karp
Date created: February 15, 2024

Time Complexity: O(N+M)
Use Cases:
1. Substring Matching: It's commonly used to find occurrences of a substring within a larger string.
2. Plagiarism Detection: Rabin-Karp is efficient for detecting similar text fragments in a large body of text, making it useful in plagiarism detection systems.
3. Rolling Hash: Because of its ability to compute hash values efficiently in a rolling fashion, Rabin-Karp is employed in various applications requiring hash-based operations on sliding windows.
"""

class RabinKarp:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.d = 256        #Number of characters in the alphabet
        self.q = 9997       #Prime number

    def search(self):
        n = len(self.text)
        m = len(self.pattern)
        p = 0
        t = 0
        h = 1

        # Calculate hash value for pattern and first window of text
        for i in range(m):
            p = (self.d * p + ord(self.pattern[i])) % self.q
            t = (self.d * t + ord(self.text[i])) % self.q

        # Calculate h = pow(d, M-1)%q
        for i in range(m-1):
            h = (h * self.d) % self.q

        # Slide the pattern over text one by one
        for i in range(n-m+1):
            if p == t:
                match = True
                for j in range(m):
                    if self.text[i+j] != self.pattern[j]:
                        match = False
                        break

                if match:
                    print("Pattern found at index", i)

            if i < n - m:
                t =(self.d * (t - ord(self.text[i]) * h) + ord(self.text[i+m])) % self.q
                if t < 0:
                    t += self.q

rk = RabinKarp("AABAACAADAABAABA", "AABA")
rk.search()