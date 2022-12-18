# Модуль для ввода/вывода информации


def choose() -> str:
    """"Выбор режима работы приложения"""
    return input("Выберете  режим работы приложения: " )


def get_expr() -> str:
    """"Запрашивает у пользователя задачу"""
    return input("Введите  задачу: " )


def show_res(res: str):
    """Выводит результат"""
    print(res)


def erorr_mode():
    """Выводит сообщение об ошибке выбора режима"""
    print('Ошибка выбора режима!')


def show_history(history: str):
    """Выводит истроии оперций"""
    print(history)
