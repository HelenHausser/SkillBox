# вводим любое число
number = int(input("Введите число: "))
# итоговая сумма чисел
summ = 0
# организуем цикл по цифрам
while number != 0:
    last_number = number % 10
    print(last_number)
    if last_number == 5:
        print("Обнаружен разрыв")
        break
# считаем сумму цифр
    summ += last_number
    number //= 10
print(summ)