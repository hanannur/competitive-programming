class Solution:
    def sortSentence(self, s: str) -> str:
        word=s.split()
        sorted_word=sorted(word ,key=lambda x : int(x[-1]))
        current_words=[words[:-1] for words in sorted_word ]
        return ' '.join(current_words)

