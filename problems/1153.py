class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        conversion_map = {}
        if len(str1) != len(str2):
            return False

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] not in conversion_map:
                    conversion_map[str1[i]] = str2[i]

                if conversion_map[str1[i]] != str2[i]:
                    return False

        if len(set(str2)) == 26 and len(conversion_map) != 0:
            return False

        return True