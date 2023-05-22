"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    all_sales = 0

    for sum_sales in sales:
        sales_list = our_sum(sum_sales['items_sold'])
        all_sales += sales_list
        print(f'Cуммарное продаж для {sum_sales["product"]}: {sales_list}')

    print('-' * 45)
    for avg in sales:
        avg_sales = our_sum(avg['items_sold']) / len(avg['items_sold'])
        print(f'Cреднее кол-во продаж {avg["product"]}: {avg_sales:,.2f}')
    all_avg = avg_sales / len(sales)
    print('-' * 45)
    print(f'Cуммарное кол-во продаж всех товаров: {all_sales}')
    print('-' * 45)
    print(f'Cреднее количество продаж всех товаров: {all_avg:,.2f}')


def our_sum(items_sold):
    individual_sales = 0
    for sold in items_sold:
        individual_sales += sold
    return individual_sales


if __name__ == "__main__":
    main()
