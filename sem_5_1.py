# Обязательная:
# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

a = '1серг. получилабв и нашел2 абвкупил ивышел на абв когда получил4 абв.'
index_gap = []
index_not_abv = []
# print(type(a))
a_1 = a.split()
# print(type(a_1))
# print(a_1)

for index, element_ in enumerate(a):
    # print(index, element_)
    if element_ == " ":
        # print(index, element_)
        index_gap.append(index)
print("индексы пробелов = ",index_gap)

# for k in a_1:
#     if "абв" not in k:
#         # print(k)
#         index_not_abv.append(k)
# print(index_not_abv)

# text_not_abv = list(lambda a_1: a_1 if "абв" not in a_1 else 0)
# print(text_not_abv(a_1))

# text_not_abv = list(map(lambda kk: kk if "абв" not in kk else "0", a_1)) 888888888
# print('текст без "абв" =',text_not_abv)

text_not_abv = list(filter(lambda kk: True if "абв" not in kk else False, a_1))
# print('текст без "абв" =',text_not_abv)
ss = str(' '.join(text_not_abv))
print('текст без "абв" =', ss)

# text_not_abv = list(filter(lambdaa : True if a == " " , a))