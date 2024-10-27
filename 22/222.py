def filter_2(func,X):
    return list(filter(func,X))

#test
X=["b b2848","adcdefg","little","egg"]
#Исключить строки с пробелами
print(filter_2(lambda s: ' ' not in s, X))

#Исключить строки, начинающиеся с буквы “a”
print(filter_2(lambda s: not s.startswith('a'), X))

#Исключить строки, длина которых меньше 5
print(filter_2(lambda s: len(s) >= 5, X))