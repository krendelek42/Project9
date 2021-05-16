def MENU():
    '''
    :return: Displays information on application usage.
    '''
    print('Навигатор:', '1. Увеличить прибыль', '2. Уменьшить прибыль', '3. Изменить цену товара', '4. Выести смету',
          '5. Вывести прибыль', '6. Закрыть программу', sep='\n')

def get_command():
    '''
    :return: Accepts a command number.
    '''
    q = False
    while q != True:
        num = input('Выберите пункт: ')
        try:
            num = int(num)
            if num <= 6 and num >= 1:
                a = True
            else:
                a = False
            if a == False:
                print('Номер введен ошибочно. Повторите попытку.')
                num = int(input('Выберите пункт: '))
        except ValueError:
            print('Введенное "{}" не является числом. Повторите попытку.'.format(num))
        else:
            q = True
    if num == 6:
        return 'QUIK'
    return num

def increase(price_with_product):
    '''
    :param price_with_product: A dictionary where keys are products and values are prices.
    :return: A function that calculates how much to change prices.
    '''
    delta = int(input('Введите насколько планируете изменить прибыль:'))
    count = len(price_with_product)
    return delta // count

def navigation(n, list_product, price_with_product, all_product):
    '''
    :param n: Team number.
    :param list_product: A dictionary where keys are departments and values are products.
    :param price_with_product: A dictionary where keys are products and values are prices.
    :param all_product: List of all products from all departments.
    :return: A function that takes a command number and executes it.
    '''
    if n == 1:
        delta_new_price = increase(price_with_product)
        print('На {} рублей следует увеличить цены'.format(delta_new_price))
        answer = input('Хотите увеличить цены? ')
        if answer.lower() == 'да':
            for name in all_product:
                old_prise = price_with_product[name]
                price_with_product[name] = old_prise + delta_new_price

    if n == 2:
        delta_new_price = increase(price_with_product)
        print('На {} рублей следует уменьшить цены'.format(delta_new_price))
        answer = input('Хотите уменьшить цены? ')
        if answer.lower() == 'да':
            for name in all_product:
                old_prise = price_with_product[name]
                price_with_product[name] = old_prise - delta_new_price
    if n == 3:
        name = input('Введите название товара: ')
        if name in price_with_product:
            new_price = int(input('Введите новую цену: '))
            price_with_product[name] = new_price
        else:
            print('Данного продукта нет')
    if n == 4:
        smeta(list_product, price_with_product)
    if n == 5:
        print('Ваша прибыль составляет {} рублей'.format(profit(price_with_product)))


def create_list():
    '''
    :return: Function for creating lists.
    '''
    keys = []
    a = True
    while a != False:
        key = input()
        if key != '':
            keys.append(key)
        else:
            a = False
    return keys

def create_dic(dic, key, value):
    '''
    :param dic: A dictionary to which new values and keys are added.
    :param key: List of keys.
    :param value: List of value.
    :return: Function for creating dictionaries.
    '''
    if len(key) == 0 and len(value) == 0:
        return dic
    dic[key[0]] = value[0]
    return create_dic(dic, key[1:], value[1:])

def get_value(dic, lis):
    '''
    :param dic: The dictionary from which the values are pulled.
    :param lis: The dictionary from which the values are pulled.
    :return: A function that pulls values from a dictionary.
    '''
    for i in dic:
        x = dic[i]
        if len(x) == 1:
            lis.append(x)
        else:
            for i in x:
                lis.append(i)
    return lis

def smeta(list_product,price_with_product):
    '''
    :param list_product: A dictionary where keys are departments and values are products.
    :param price_with_product: A dictionary where keys are products and values are prices.
    :return: A function that displays a list of products with a price.
    '''
    print('{:^31}'.format('СМЕТА'))
    print('|{:^15}|{:^10}|{:^6}|'.format('Отдел', 'Продукт', 'Цена'))
    for i in list_product:
        print('|{:^15}|{:^10}|{:^6}|'.format(i, '', ''))
        x = list_product.get(i)
        if len(list(x)) == 1:
            p = price_with_product.get(x)
            print('|{:^15}|{:<10}|{:^6}|'.format('',x,p))
        else:
            for i in x:
                p = price_with_product.get(i)
                print('|{:^15}|{:<10}|{:^6}|'.format('',i,p))

def profit(price_with_product):
    '''
    :param price_with_product: A dictionary where keys are products and values are prices.
    :return: A function that calculates profit.
    '''
    prices = []
    prices = get_value(price_with_product, prices)
    num = 0
    for i in prices:
        num += i
    return num


def main():
    '''
    :return: The main function.
    '''
    print('Введите названия отделов')
    depart = create_list()
    product = []
    print('Введите названия продуктов')
    n = 0
    for i in range(len(depart)):
        print(depart[n], ':', sep = '')
        product_of_depart = create_list()
        product.append(product_of_depart)
        n += 1
    list_product = {}
    list_product = create_dic(list_product, depart, product)
    print('Введите цены продуктов: ')
    all_product = []
    all_product = get_value(list_product, all_product)
    price = []
    n = 0
    for i in range(len(all_product)):
        print(*all_product[n], ':', sep= '')
        num = int(input())
        price.append(num)
        n += 1
    price_with_product = {}
    price_with_product = create_dic(price_with_product, all_product, price)
    while True:
        MENU()
        command = get_command()
        if command == 'QUIK':
            print()
            print('Работа программы завершена.')
            break
        navigation(command, list_product, price_with_product, all_product)

main()



