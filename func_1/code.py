def words_counter(input_line='one two one tho three'):
    # Подготавливаем словарь для сбора отдельных слов и их подсчёта
    words_dict = dict()
    # Подготавливаем пустую строку для сбора результатов подсчёта
    count_str = ''

    # Разделяем входное предложение на отдельные слова и итерируем каждое слово
    for word in input_line.split():
        if word not in words_dict:
            # Если текущее слово ещё не находится в словаре, тогда присваиваем счётчик как 0
            words_dict[word] = 0
        else:
            # Если текущее слово есть уже в словаре, тогда увеличиваем счётчик на 1
            words_dict[word] += 1
        # добавляем результат в строку count_str для текущего слова
        count_str += str(words_dict[word]) + ' '
    # Возвращаем результат
    return count_str
