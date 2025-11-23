
from collections import deque

def is_palindrome(input_string:str):
    # Видаляємо пробіли та переводимо рядок до нижнього регістру
    cleaned_string = ''.join(input_string.split()).lower()
    
    # Ініціалізуємо двосторонню чергу
    char_deque = deque(cleaned_string)
    
    while len(char_deque) > 1:
        # Порівнюємо символи з обох кінців черги
        if char_deque.popleft() != char_deque.pop():
            return False
    return True
# Приклади використання
print(is_palindrome("А роза упала на лапу Азора"))  # True