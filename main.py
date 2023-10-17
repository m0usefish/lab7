
countries_data = {
    "Україна": {"населення": 44.03, "площа": 603.5},
    "Португалія": {"населення": 10.4, "площа": 92.3},
    "Китай": {"населення": 125.78, "площа": 377.9},
    "США": {"населення": 328.2, "площа": 9831.7},
    "Японія": {"населення": 1380.00, "площа": 3287},
    "Бразилія": {"населення": 210.14, "площа": 8515},
    "Франція": {"населення": 67.34, "площа": 551.7},
    "Німеччина": {"населення": 83.02, "площа": 357.5},
    "Канада": {"населення": 37.59, "площа": 9984},
    "Австралія": {"населення": 25.41, "площа": 2968.7}
}
def print_dictionary(data):
    for country, details in data.items():
        print(f"{country}: Населення - {details['населення']} мільйони(ів), Площа - {details['площа']} тисяч квадратних кілометрів")

def add_country():
    country = input("Введіть країну: ")
    population = input("Введіть населення: ")
    while int(population) < 0:
        population = input("Чисельність населення не може бути менше 0, введіть ще раз: ")
    area = input("Введіть площу: ")
    while int(area) < 0:
        area = input("Площа не може бути менше 0, введіть ще раз: ")
    if country in countries_data:
        print(f"{country} вже існує в словнику, якщо бажаєте оновити інформацію - натисніть 1, якщо ні, натисніть будь-яку іншу цифру")
        ans = input("Ваша відповідь: ")
        while ans.isalpha():
            ans = input("Введіть ще раз (цифру): ")
        if ans == str(1):
            countries_data[country] = {"населення": population, "площа": area}

            print(f"Елемент {country} додано до словника.")
    else:
        countries_data[country] = {"населення": population, "площа": area}

        print(f"Елемент {country} додано до словника.")
def delete_country():
    country = input("Введіть країну, яку хочете видалити: ")
    if country in countries_data:
        del countries_data[country]
        print(f"Видалено {country} зі словника.")
    else:
        print(f"{country} не існує в словнику.")
def sort_dictionary(data):
    sorted_data = {k: v for k, v in sorted(data.items())}

    print("Відсортований словник за назвою країни: ")
    print_dictionary(sorted_data)

def max_population_density(data):
    max_density = 0
    max_density_country = ""
    for country, details in data.items():
        population = details['населення']
        area = details['площа']
        density = int(population) / int(area)

        if density > max_density:
            max_density = density
            max_density_country = country

    if max_density_country:
        print(f"Країна з найбільшою щільністю населення {max_density_country} \nщільність = {max_density:.2f} мільйона на один квадратний кілометр.")
    else:
        print("Недостаньо інформації для розрахунків.")

menu_choice = 0

while menu_choice != 6:
    print("Меню:")
    print("1. Вивести на екран всі значення словника")
    print("2. Додати елемент")
    print("3. Видалити елемент ")
    print("4. Відсортувати словник ")
    print("5. Визначити країну з максимальною щільністю населення ")
    print("6. Завершити програму")

    try:
        menu_choice = int(input("Оберіть опцію: "))

        if menu_choice == 1:
            if countries_data:
                print_dictionary(countries_data)
            else:
                print("Дані відсутні.")
        elif menu_choice == 2:
            add_country()
        elif menu_choice == 3:

            delete_country()
        elif menu_choice == 4:
            sort_dictionary(countries_data)
        elif menu_choice == 5:
            max_population_density(countries_data)
        elif menu_choice == 6:
            print("Програма завершена.")
        else:
            print("Неправильний вибір. Виберіть 1, 2 або 3.")
    except ValueError:
        print("Неправильний ввід. Виберіть 1, 2 або 3.")

