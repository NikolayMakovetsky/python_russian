import re

text = """История России насчитывает более тысячи лет, начиная с переселения восточных славян
 на Восточно-Европейскую равнину в VI—VII веках, впоследствии разделившихся на русских,
украинцев и белорусов[1]. История страны разделяется примерно на семь периодов:
 древнейший (догосударственный) (до конца IX века н. э.) период,
период Киевской Руси (до середины XII века), период раздробленности (до начала XVI века),
период единого Русского государства (с 1547 года царства) (конец XV века — 1721),
 период Российской империи (1721—1917), советский период (1917—1991) и новейшая история (с 1991 года).
"""

info = "10 EUR 20 EUR 30 EUR - EURO EUROPE"

text_2 = '''Знаки препинания: первая и вторая запятая - причастный оборот, третья запятая - подчинительная
 связь между предложениями, четвертая запятая - сочинительная связь между предложениями, пятая запятая - 
 сочинительная связь между предложениями, шестая запятая - подчинительная связь между предложениями, седьмая
запятая - подчинительная связь между предложениями.'''

print("\n---find years in text")
years = re.findall(r'\d{4}', text) # используем r'', т.к. в регулярках часто используется символ '\'
print(years)

print("\n---find periods in text")
periods = re.findall(r'\d{4}—\d{4}', text)
print(periods)

print("\n---change EUR to USD in info")
print(info.replace('EUR', 'USD')) # 'USDO USDOPE' - incorrect!
result = re.sub(r'\bEUR\b', 'USD', info) # \b обозначает некие границы слова (пробелы, запятые, точки и т.д.)
print(result) # SUB = SUBSTITUTION (ЗАМЕНА)
