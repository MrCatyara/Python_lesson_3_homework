import pymorphy2
import regex as re

# Считаем текст из файла

file1 = open('String.txt', 'r', encoding = 'utf-8')
String = file1.read()
file1.close()
# применим "re" для отделения всех цифр и букв алфавита от остальных знаков
# ключ w это Любая цифра или буква (\W — все, кроме буквы или цифры)
# ключ + это 1 и более вхождений шаблона слева

string_list = re.findall(r'\w+', String)
string_list_lower = list(map(lambda s:s.lower(),string_list))

morph = pymorphy2.MorphAnalyzer()

String_lemm = []
for i in string_list_lower:
    String_lemm.append(morph.parse(i)[0].normal_form)


#print(string_list_lower)
#print(String_lemm)

String_dict = {}
for i in String_lemm:
    i2 = String_dict.get(i,0)
    String_dict[i] = i2 + 1

# print(String_dict)

String_obj = String_dict.items()
String_sort = sorted(String_obj,key=lambda s:s[1],reverse=True)
for i in range(5):
    print('Слово "{}" встречается {} раз'.format(String_sort[i][0],String_sort[i][1]))

print('Всего встречается {} разных слов'.format(len(String_dict)))


