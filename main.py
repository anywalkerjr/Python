meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "ЩИЩ": "Одобрение или восторг",
            "КРИПОВЫЙ": "Страшный, пугающий",
            "АГРИТЬСЯ": "Злиться",
            "ВАЙБ": "Атмосфера",
            "АБЬЮЗЕР": "Это человек, использующий критику, обвинения в целях манипулирования людьми",
            "ИМБА": "Что-то очень крутое",
            "ЖИЗА": "Ситуация, актуальная для слушателя",
            "КРАШ": "Человек, к которому испытывают симпатию"
            }
for i in range(0,5):
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        print(word, '-', meme_dict[word])
    else:
        print('Такого слова еще нет в нашем словаре!')
