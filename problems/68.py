class Solution:
    def justify_line(self, current_line_width_wo_spaces, number_of_words_in_line, maxWidth, justify_left=False):
        if len(number_of_words_in_line) == 1 or justify_left:
            number_of_words_in_line[-1] = number_of_words_in_line[-1] + ' ' * (maxWidth - (current_line_width_wo_spaces + len(number_of_words_in_line) - 1))
            string = ' '.join(number_of_words_in_line)
        else:
            delimiter_size = (maxWidth - current_line_width_wo_spaces) // (len(number_of_words_in_line) - 1)
            one_more_longer_delimiters = (maxWidth - current_line_width_wo_spaces) % (len(number_of_words_in_line) - 1)

            for i in range(len(number_of_words_in_line) - 1):
                if one_more_longer_delimiters:
                    number_of_words_in_line[i] = number_of_words_in_line[i] + " " * (delimiter_size + 1)
                    one_more_longer_delimiters -= 1
                else:
                    number_of_words_in_line[i] = number_of_words_in_line[i] + " " * delimiter_size

            string = ''.join(number_of_words_in_line)

        return string

    def fullJustify(self, words, maxWidth: int):
        justified = []
        current_line_width_wo_spaces = 0
        number_of_words_in_line = []

        for word in words:
            if current_line_width_wo_spaces + len(number_of_words_in_line) + len(word) > maxWidth:
                justified.append(self.justify_line(current_line_width_wo_spaces, number_of_words_in_line, maxWidth))
                current_line_width_wo_spaces = 0
                number_of_words_in_line.clear()

            current_line_width_wo_spaces += len(word)
            number_of_words_in_line.append(word)

        if number_of_words_in_line:
            justified.append(self.justify_line(current_line_width_wo_spaces, number_of_words_in_line, maxWidth, justify_left=True))
        return justified


if __name__ == '__main__':
    s = Solution()
    for string in s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16):
        print(string, len(string))

    print('---------------------')
    for string in s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16):
        print(string, len(string))

    print('---------------------')
    for string in s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"], 20):
        print(string, len(string))

    print('---------------------')
    for string in s.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16):
        print(string, len(string))
