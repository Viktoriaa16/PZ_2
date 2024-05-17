# 24
# В исходном текстовом файле Dostoevsky.txt найти все годы деятельности писателя
# ( например, 1821 года, 1837 год, 1843 году и так далее по всему тексту)
# Почитать количество полученных элементов

import re
with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    years = re.findall(r'\b\d{4}\s*(?:год(?:а|у)?)?\b', text)
print(len(years))
for year in years:
    print(year)