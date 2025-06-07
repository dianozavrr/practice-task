# Task2.py

def find_pythagorean_triplets(n):
    """
    Знаходить усі піфагорові трійки (a, b, c) такі, що:
    a^2 + b^2 = c^2 і всі числа не перевищують n.
    """
    triplets = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):  # починаємо з a, щоб уникнути дублікатів
            c_squared = a  2 + b  2
            c = int(c_squared  0.5)
            if c <= n and c  2 == c_squared:
                triplets.append((a, b, c))
    return triplets


# Приклад використання
if name == "main":
    n = 30
    result = find_pythagorean_triplets(n)
    print("Піфагорові трійки:")
    for triplet in result:
        print(triplet)
