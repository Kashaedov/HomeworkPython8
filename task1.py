
print ("Основый ингридиент:\nКапуста\nГорох\nСвекла\nГрибы\nРыба\nНичего")
maimIngridients = {'Капуста': 'Щи', 'Горох': 'Гороховый', 'Свекла': 'Борщ', 'Грибы': 'Грибной суп', 'Рыба': 'Уха', 'Ничего': 'Обычный кипяток'}
class Soup:
    def show_my_soup(self, ingridient):
        print(f'Ваш суп - {maimIngridients[ingridient]}')

while True:
    choice = input('Выберите основной ингридиент: ').capitalize()
    temp = []
    for prod in maimIngridients.keys():
        temp.append(prod)
    res = choice in temp
    if res == False:
        print('Мы еще не все умеем. Введите ингридиент из перечисленных выше!')
    else:
        break
my_soup = Soup()
my_soup.show_my_soup(choice)

