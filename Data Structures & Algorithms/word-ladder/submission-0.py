class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        q=deque()
        q.append((beginWord,1))
        while len(q)!=0:
            currword,level=q.popleft()
            if currword==endWord:
                return level
            for i in range(0,len(currword)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch==currword[i]:
                        continue
                    newword=currword[:i]+ch+currword[i+1:]
                    if newword in wordset:
                        q.append((newword,level+1))
                        wordset.remove(newword)
        return 0