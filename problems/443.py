def _compress(chars, i, picked_char, picked_char_count):
    chars[i] = picked_char
    i += 1
    ranks = []
    if picked_char_count > 1:
        while picked_char_count > 0:
            ranks.append(picked_char_count % 10)
            picked_char_count //= 10

        for r in reversed(ranks):
            chars[i] = str(r)
            i += 1

    return i


class Solution:
    def compress(self, chars) -> int:
        if not chars:
            return []

        i = 0  # end of compressed string

        picked_char = chars[i]
        picked_char_count = 0
        for j in range(len(chars)):
            if chars[j] == picked_char:
                picked_char_count += 1

            if chars[j] != picked_char:
                i = _compress(chars, i, picked_char, picked_char_count)

                picked_char = chars[j]
                picked_char_count = 1

            if j == len(chars) - 1:
                i = _compress(chars, i, picked_char, picked_char_count)

        while i != len(chars):
            chars.pop()

        return i