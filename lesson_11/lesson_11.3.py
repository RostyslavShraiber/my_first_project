def is_even(number: int) -> bool:
    """
    Перевіряє, чи є число парним.

    Параметри:
    number (int): Число для перевірки.

    Повертає:
    bool: True, якщо число парне, False, якщо непарне.
    """
    return str(number)[-1] in {'0', '2', '4', '6', '8'}


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("OK")
