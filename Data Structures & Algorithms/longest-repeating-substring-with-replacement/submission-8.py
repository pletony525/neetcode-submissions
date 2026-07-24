class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #What do we want to do. Want to keep track of unique characters.
        #Do this by expanding window if k > 0 and shrinking if k ==0 

        maxFreq = 0
        windowSize = 0
        frequencyTable = {}
        s = list(s)
        for r in range(len(s)):
            frequencyTable[s[r]] = frequencyTable.get(s[r], 0) + 1
            windowSize += 1
            maxFreq = max(maxFreq, frequencyTable.get(s[r]))
            valid = windowSize - maxFreq <= k
            if not valid:
                firstIndex = r - windowSize + 1
                frequencyTable[s[firstIndex]] = frequencyTable.get(s[firstIndex]) - 1
                windowSize -= 1
        return windowSize


             
            