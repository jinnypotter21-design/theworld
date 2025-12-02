#1
numbers = [17, 25, 20, 3, 48]


try:

    total = sum(numbers)
    print(f"Сумма элементов списка: {total}")
except TypeError as e:
    print(f"Ошибка: в списке обнаружен элемент, который не является числом. {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

#4

numbers = [10, 25, 5, 34, 47]

print("Список чисел:", numbers)

try:

    user_input = input("Введите число для поиска: ")


    search_number = float(user_input)


    if search_number in numbers:
        print(f"Число {search_number} есть в списке!")
    else:
        print(f"Число {search_number} не найдено в списке.")

except ValueError:
    print("Ошибка: вы ввели не число. Пожалуйста, введите корректное числовое значение.")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")


#8
numbers = []

print("Введите 10 целых чисел:")

for i in range(10):
    while True:
        try:
            user_input = input(f"Введите число {i + 1}: ")
            number = int(user_input)
            numbers.append(number)
            break
        except ValueError:
            print("Ошибка: введено не целое число. Пожалуйста, введите целое число снова.")
        except KeyboardInterrupt:
            print("Программа прервана пользователем.")
            exit()
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

# Выводим итоговый список
print(f"Список из 10 целых чисел: {numbers}")
