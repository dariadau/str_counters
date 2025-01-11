def check_index(input_line="one two one tho three"):
    words_dict = {}
    count_lst = ['-1'] * len(input_line.split())

    for idx, word in enumerate(input_line.split()):
        if word not in words_dict:
            words_dict[word] = idx
        else:
            count_lst[idx] = str(words_dict[word])
            words_dict[word] = idx
    return ', '.join(count_lst)
