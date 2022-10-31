class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def F(s):
            skip = 0
            for x in reversed(s):
                if x == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return all(x == y for x, y in itertools.zip_longest(F(s),F(t)))