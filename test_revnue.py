import pytest
from revenue import revenue

@pytest.mark.parametrize("n, m, x, expected", [
    (30, 10, 10000, 330000),  # Пример из задачи
    (1, 10, 5000, 5000),      # Один этаж
    (5, 2, 10000, 51000),     # Пять этажей, рост каждые 2 этажа
    (20, 5, 10000, 220000),   # Двадцать этажей, рост каждые 5 этажей
    (50, 10, 12000, 690000)   # 50 этажей, цена растёт каждые 10 этажей
])

def test_revenue(n, m, x, expected):
    assert revenue(n, m, x) == expected