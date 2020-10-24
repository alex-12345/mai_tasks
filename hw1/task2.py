first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print("Минимум: " + str(first_number if(first_number < second_number) else second_number))