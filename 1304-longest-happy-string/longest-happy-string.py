class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ''
        while a > 0 or b > 0 or c > 0:
            if a >= b and a >= c:
                if len(s) >= 2 and s[-2:] == 'aa':
                    if b > c:
                        s += 'b'
                        b -= 1
                    elif c > 0:
                        s += 'c'
                        c -= 1
                    else:
                        break
                else:
                    s += 'a'
                    a -= 1

            elif b >= a and b >= c:
                if len(s) >= 2 and s[-2:] == 'bb':
                    if a > c:
                        s += 'a'
                        a -= 1
                    elif c > 0:
                        s += 'c'
                        c -= 1
                    else:
                        break
                else:
                    s += 'b'
                    b -= 1

            elif c >= a and c >= b:
                if len(s) >= 2 and s[-2:] == 'cc':
                    if a > b:
                        s += 'a'
                        a -= 1
                    elif b > 0:
                        s += 'b'
                        b -= 1
                    else:
                        break
                else:
                    s += 'c'
                    c -= 1

        return s
        