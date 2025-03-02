def revenue(n: int, m: int, x: int) -> int:
    total = 0  # Начальная сумма
    for floor in range(1, n + 1):  
        price = x + ((floor - 1) // m) * 1000  
        total += price  
    return total