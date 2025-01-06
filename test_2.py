import pytest
from main_2 import count_vowels  # Импорт функции из вашего основного файла

def test_count_vowels_only_vowels():
    # Строка, состоящая только из гласных
    assert count_vowels("aeiouAEIOU") == 10  # 5 строчных и 5 прописных гласных

def test_count_vowels_no_vowels():
    # Строка, не содержащая гласных
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0  # Нет гласных

def test_count_vowels_mixed_case():
    # Строка с гласными в разных регистрах
    assert count_vowels("Hello World") == 3  # 'e', 'o', 'o' - 3 гласных

def test_count_vowels_empty_string():
    # Пустая строка
    assert count_vowels("") == 0  # Нет гласных, результат 0
