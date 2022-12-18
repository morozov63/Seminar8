def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    with open('file.txt', 'a') as data: 
         data.write(f'{expr} -> {result}\n') 
    
def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('file.txt', 'r') as data: 
         return (data.read())
