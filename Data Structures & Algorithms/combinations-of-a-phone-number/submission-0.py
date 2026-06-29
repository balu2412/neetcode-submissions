class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []
        self.backtrack(0, "",digit_to_letters,digits,res)
        return res
    def backtrack(self,idx, comb,digit_to_letters,digits,res):
        if idx == len(digits):
            res.append(comb[:])
            return
  
        for letter in digit_to_letters[digits[idx]]:
            self.backtrack(idx + 1, comb + letter,digit_to_letters,digits,res)