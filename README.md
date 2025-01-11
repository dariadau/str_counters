# str_counters (строковые счетчики)
str_counters состоит из $${\color{purple}3 \space функций}$$, которые могут совершать следующие действия со строками:

#  1. **Что делает words_counter?**        
   Текст приводится в одной строке. Для каждого слова текста подсчитывается количество его вхождений перед ним.        
   Слово - это последовательность символов, не содержащих пробелов. Два последовательных слова разделяются одним или несколькими пробелами.        

> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}str}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _"one two one tho three"_        

> [!TIP]  
> **Пример ввода-вывода:**       
> $${\color{lightgreen}input:}$$ _"one two one tho three"_       
> $${\color{lightgreen}output:}$$ _0 0 1 0 0_
	
	
# 2. **Что делает count_repeats?**        
   Текст приводится в одной строке. Выведите слово в тексте, которое встречается чаще всего.	
   Если таких слов много, выведите то, которое меньше в алфавитном порядке.	
   
> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}str}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _"apple orange banana banana orange"_

> [!TIP]      
> **Пример ввода-вывода:**        
> $${\color{lightgreen}input:}$$ _"apple orange banana banana orange"_       
> $${\color{lightgreen}output:}$$ _banana_

   
# 3. **Что делает check_index?**        
   Текст приводится в одной строке. Для каждого слова из этого текста найдите индекс его предыдущего появления в тексте.        
   Индекс первого слова равен 0. Если слово встречается один раз, выведите значение -1.        

> [!NOTE]
> Пользователем задается $${\color{lightblue}один \space аргумент}$$ типа $${\color{lightblue}str}$$    
> $${\color{lightblue}Значение \space по \space умолчанию:}$$ _"one two one tho three"_        

> [!TIP]
> **Пример ввода-вывода:**        
> $${\color{lightgreen}input:}$$ _"one two one tho three"_       
> $${\color{lightgreen}output:}$$ _-1 -1 0 -1 -1_
