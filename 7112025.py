
#1
def print_quote():
    print("“Don't let the noise of others' opinions")
    print("drown out your own inner voice.”")
    print("Steve Jobs")


print_quote()

#2
def print_odd_numbers(start, end):

    if start > end:
        start, end = end, start


    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)



print(print_odd_numbers(3, 10))

#3

def draw_line(length, direction, symbol):
    if direction == 'h':
        print(symbol * length)
    elif direction == 'v':
        for _ in range(length):
            print(symbol)
    else:
        print("Ошибка: направление должно быть 'h' (горизонталь) или 'v' (вертикаль)")


draw_line(5, 'h', '*')
draw_line(3, 'v', '#')

#4

def max_of_four(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum

print(max_of_four(4, 5, 6, 7))


#5

def sum_in_range(start, end):

    if start > end:
        start, end = end, start
    return sum(range(start, end))


result = sum_in_range(1, 5)
print("Сумма чисел от 1 до 5:", result)


#6

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False


    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(10))
print(is_prime(1))

#7

def is_lucky_number(number):

    if not (100000 <= number <= 999999):
        return False


    num_str = str(number)


    first_half = sum(int(digit) for digit in num_str[:3])
    second_half = sum(int(digit) for digit in num_str[3:])

    return first_half == second_half



print(is_lucky_number(123420))
print(is_lucky_number(723422))
print(is_lucky_number(123))


