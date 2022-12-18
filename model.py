# Модуль для выполнения опреаций


def execute_expr(expr: str) -> str:         
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    return str(eval(expr))

import sympy 
def solve_eq(expr: str) -> str:                  
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    #expr = input('Enter expr: ')
    expr = expr.replace ('=', ' ' )# можно было и с помощью expr.removesuffix('= 0'), но могут и ввести без пробелов
    expr = expr.replace ('0', ' ' )
    x = sympy.Symbol('x')
    try:
       ans = (sympy.solve(expr, x))
       return ','.join(str(x) for x in ans)  
    except ValueError:
       print('Incorrect input')



def simpify_pol(expr: str) -> str:           
    """"Упрощает введенный многочлен"""
    x = sympy.Symbol('x')
    try:
       ans = sympy.simplify(expr)
       return ans
    except ValueError:
       print('Incorrect input')
