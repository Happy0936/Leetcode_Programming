class Solution(object):
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

    
        suffix = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suffix[i] += 1
                j -= 1

        ans = []
        pos = 0
        changed = False

        for i in range(m):

            while pos < n:

        
                if word1[pos] == word2[i]:
                    ans.append(pos)
                    pos += 1
                    break

                if not changed:
                    remaining = m - i - 1

                    if suffix[pos + 1] >= remaining:
                        ans.append(pos)
                        pos += 1
                        changed = True
                        break

                pos += 1

            else:
                return []

        return ans