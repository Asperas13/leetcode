#
#     ^
# stars = []
# stack = [(]

class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets = []
        stars = []

        for i in range(len(s)):
            if s[i] == '(':
                open_brackets.append(i)
            elif s[i] == '*':
                stars.append(i)
            else:
                if open_brackets:
                    open_brackets.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        if len(open_brackets) == 0:
            return True

        while open_brackets and stars:
            bracket, star = open_brackets.pop(), stars.pop()
            if star < bracket:
                return False

        return len(open_brackets) == 0