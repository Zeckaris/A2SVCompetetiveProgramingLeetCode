class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list[str]:
        words_A = A.split()
        words_B = B.split()
        count_A = {}
        count_B = {}
        
        for word in words_A:
            count_A[word] = count_A.get(word, 0) + 1

        for word in words_B:
            count_B[word] = count_B.get(word, 0) + 1
        result = []

        for word in count_A:
            if count_A[word] == 1 and count_B.get(word, 0) == 0:
                result.append(word)

        for word in count_B:
            if count_B[word] == 1 and count_A.get(word, 0) == 0:
                result.append(word)

        return result
