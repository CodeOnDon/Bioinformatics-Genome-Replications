# BetterFrequentWords


# BetterFrequentWords takes a text as a string and a k value as an integer. Then returns an array of k-mer patterns that were the most frequent in text.
# INPUT: Text as a string and the k as an integer representing the pattern length
# OUTPUT: An array with k-mers that were most frequent in the text string
def BetterFrequentWords(text: str, k: int) -> list:
    freqPatterns = [] # an empty arrayt (list) for now
    freqMap = FrequencyTable(text, k)
    max_freq = MaxMap(freqMap)

    for pattern,count in freqMap.items():
        if count == max_freq:
            freqPatterns.append(pattern)

    return freqPatterns

# FrequencyTable takes a text as a string and k as the length of the patterns we will look for, the outpuit is a table that has the freq of each pattern
# INPUT: Text as a string and k as an int for the lenth of the patterns
# OUTPUT: A table having each pattern of length k from left to right of the string and its corresponding frequency
def FrequencyTable(text: str, k: int) -> dict:
    freqMap = {}
    n = len(text)

    for i in range(n-k+1):
        pattern = text[i:i+k]
        if pattern not in freqMap:
            # if the pattern has not appeared before than this is the first occurance
            freqMap[pattern] = 1
        else:
            freqMap[pattern] += 1

    return freqMap



# MaxMap takes a freqTable as a dictionary as input, and returns the the value of the greatest frequency in the table
# INPUT: Dictionary containing patterns as keys and thier frequency as values
# OUTPUT: The maximum value in the dictionary representing the max frequency value
def MaxMap(freqTable: dict) -> int:
    max = 0
    for freq in freqTable.values():
        if freq > max:
            max = freq
    return max


# CountPattern takes a text and a pattern both as strings as input and returns the number of times the pattern was found in the text
# INPUT: Text as a string and pattern as a string
# OUTPUT: Number of times that pattern was found in the text string
def CountPattern(text: str, pattern: str) -> int:
    count = 0
    for i in range (len(text) - len(pattern) + 1):
        currentWindow = text[i:i + len(pattern)]
        if currentWindow == pattern:
            count += 1
    return count


testList = BetterFrequentWords("ABCDEFGHIABC", 3)
print(testList)

