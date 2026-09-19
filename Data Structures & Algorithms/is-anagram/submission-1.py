class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = s
        stringT = t

        if (len(stringS) == len(stringT)):
            for charS in stringS:
                if (stringT.count(charS) == stringS.count(charS)):
                    stringT = stringT.replace(charS, "")

                stringS = stringS.replace(charS, "")

            if (stringS == stringT):
                return True

        return False
