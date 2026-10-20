from text_utils import clean_word

def count_words(file_path, stop_words):
    unique_words = dict()
    total_words = 0

    fopen = open(file_path, "r")

    line = fopen.readline()
    while line != "":
        words = line.split()
        for raw_word in words:
            word = clean_word(raw_word)

            if not word:
                continue

            total_words += 1

            if word in stop_words:
                continue

            if word not in unique_words:
                unique_words[word] = 1
            else:
                unique_words[word] += 1
        line = fopen.readline()
    fopen.close()
    return unique_words,total_words