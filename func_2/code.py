def count_repeats(input_line="apple orange banana banana orange"):
    words_dict = dict()

    if all(len(word) == 1 for word in input_line.split()):
        print(min(input_line.split()))
    else:
        for word in input_line.split():
            if input_line.count(word) > 1:
                words_dict[word] = input_line.count(word)
        return min(sorted(words_dict))