"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""

questions_and_answers = {}

the_end = ''
while the_end != 'n':
    your_question = input('Вопрос: ')
    questions_and_answers[your_question] = input('Ответ: ')
    the_end = input('Продолжить?' 'y/n ')


def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    finish = ''
    while finish != 'n':
        try:
            search = answers_dict[input('Ваш вопрос? ')]
            print(search)
            finish = input('Продолжить?' 'y/n ')
        except KeyError:
            print('Вопрос не найден')


if __name__ == "__main__":
    ask_user(questions_and_answers)
