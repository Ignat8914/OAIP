def main ():
    lines = []

    while True:
        line = input("Введите строку (или нажмите Enter для выхода): " )
        if line == "":
            break
        lines.append(line)

    print("\nДлины введеных строк:")
    for line in lines:
        print(len(line))

if __name__=="__main__":
    main()

negative_count = 0

while True:

    number = float(input("Введите вещественное число или (число больше 36.6 для завершения): "))


    if number > 36.6:
        break


    if number < 0:
        negative_count += 1

print(negative_count)

first_max = float('-inf')
second_max = float('-inf')

while True:
    num = int(input("Введите число: "))

    if abs(num) >= 1000:
        break

    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num


if second_max == float('-inf'):
    print("Второй максимум не найден.")
else:
    print("Второй максимум:", second_max)


numbers = input("Введите числа через пробел: ")


number_list = list(map(int, numbers.split()))


if number_list:
    smallest = number_list[0]


    for num in number_list:

        if num < smallest:
            smallest = num


    print("Наименьшее число в последовательности:", smallest)
else:
    print("Список чисел пуст.")


def main():
    while True:
        number = int(input("Введите число (0 для выхода): "))

        if number == 0:
            break

        if number % 3 == 0 and number % 7 == 0:
            print("Караул!")
            break
        elif number % 3 == 0:
            print("Несчастливое")
        elif number % 7 == 0:
            print("Опасное")
        else:
            print(number)


if __name__ == "__main__":
    main()

def sum_of_primes(n):

    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:

            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1


    prime_sum = sum(p for p in range(2, n + 1) if is_prime[p])
    return prime_sum


result = sum_of_primes(10000)
print(result)


def can_fit_in_box(box_dimensions, small_boxes):
    big_box_volume = box_dimensions[0] * box_dimensions[1] * box_dimensions[2]
    total_small_boxes_volume = 0

    for box in small_boxes:
        total_small_boxes_volume += box[0] * box[1] * box[2]

    return total_small_boxes_volume <= big_box_volume



x = int(input("Введите ширину большой коробки: "))
y = int(input("Введите длину большой коробки: "))
z = int(input("Введите высоту большой коробки: "))


small_boxes = []

print("Введите размеры маленьких коробок (ширина, длина, высота). Введите 0, чтобы закончить ввод:")
while True:
    dimensions = list(map(int, input("Введите размеры: ").split()))
    if dimensions[0] == 0:
        break
    if len(dimensions) == 3:
        small_boxes.append(dimensions)


if can_fit_in_box((x, y, z), small_boxes):
    print("Да")
else:
    print("Нет")


def find_shortest_word():
    shortest_word = None

    while True:
        word = input("Введите слово (или 'стоп' для окончания ввода): ")

        if word.lower() == "стоп":
            break


        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word

    if shortest_word:
        print(f"Самое короткое слово: {shortest_word}")
    else:
        print("Слов не было введено.")


find_shortest_word()


def calculator():
    result = 0
    operation = None

    print("Введите числа и операции (например, +, -, *, /). Введите 'стоп' для выхода.")

    while True:
        user_input = input("Введите число, операцию или 'стоп': ")

        if user_input.lower() == 'стоп':
            break

        try:

            num = float(user_input)
            if operation is None:
                result = num
            else:
                if operation == '+':
                    result += num
                elif operation == '-':
                    result -= num
                elif operation == '*':
                    result *= num
                elif operation == '/':
                    if num != 0:
                        result /= num
                    else:
                        print("Ошибка: деление на ноль!")
                else:
                    print("Неизвестная операция!")
        except ValueError:

            if user_input in ['+', '-', '*', '/']:
                operation = user_input
            else:
                print("Ошибка: неверный ввод, пожалуйста, введите число или допустимую операцию.")

    print("Результат:", result)


calculator()

def main():
    sentences = []
    current_sentence = []

    while True:
        word = input()
        if word.lower() == "стоп":
            if current_sentence:
                sentences.append(" ".join(current_sentence))
            break
        current_sentence.append(word)

    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()


