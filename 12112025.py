import random
import string


def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Ошибка: Не выбраны типы символов."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def check_password_strength(password):
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    char_types = sum([has_upper, has_lower, has_digit, has_special])

    if char_types >= 4:
        score += 3
    elif char_types >= 3:
        score += 2
    elif char_types >= 2:
        score += 1

    if score >= 5:
        strength = "Сильный"
    elif score >= 3:
        strength = "Средний"
    else:
        strength = "Слабый"

    return f"{strength} (Очки: {score})"


password_strong = generate_password(length=14, use_special=True)
password_simple = generate_password(length=6, use_upper=False, use_digits=False, use_special=False)

print(f"Сильный пароль: {password_strong}")
print(f"Простой пароль: {password_simple}")
print(f"Проверка сильного: {check_password_strength(password_strong)}")
print(f"Проверка среднего: {check_password_strength('Pa$$w0rd')}")
print(f"Проверка слабого: {check_password_strength(password_simple)}")
