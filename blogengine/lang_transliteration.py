rus_symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
               'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы',
               'э', 'ю', 'я']

eng_symbols = ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'j', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'sch', 'i', 'e', 'u', 'ya']

transliterate_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y',
 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'i', 'э': 'e', 'ю': 'u', 'я': 'ya'}


def transliterate_to_eng(rus_text):
    transliterated_text = ''
    for i in rus_text.lower():
        if i in rus_symbols:
                transliterated_text += transliterate_dict.get(i)
        else:
            if i == 'ь' or i == 'ъ':
                continue
            else:
                transliterated_text += i
    return transliterated_text

