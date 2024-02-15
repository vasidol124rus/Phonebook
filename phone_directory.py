# '''Задача №55 Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
#  Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# '''

# 1.Создание файла.                             +++++++
# - открываем файл на дозапись #a, перезапись w +++++++
# 2. Добавление контакта: ++++++
# - запросить у пользователя данные котакта ++++++
# - Открыть файл на дозапись #a +++++
# - добавить новый контакт+++++
# 3. Вывод данных на экран :++++
# - открыть файл на чтение #r++++
# - считать файл +++++
# - вывести на экран+++++
# 4. Поиск контакта:
# - выбор варианта поиска
# - запросить данные для поиска
# - открываем файл на чтение, сохраняем в переменную
# - осуществляем поиск контакта
# - выводим на экран найденый контакт
# 5.Cоздание юзер интерфейса(UI):   +++++++
# - вывод меню на экран              ++++++++
# - запросить у пользователя вариант действия ++++++++
# - запустить соотетствующую функцию +++++++++++++
# - осуществить возможность выхода из программы ++++++++

def input_surname():
    return input("Введите фамилию контакта: ").title()
def input_name():
    return input("Введите имя контакта: ").title()
def input_patronymic():
    return input("Введите отчество контакта: ").title()
def input_phone():
    return input("Введите телефон контакта: ")
def input_address():
    return input("Введите адрес(город) контакта: ").title()
def create_contact():
    surname = input_surname()
    name = input_name()
    patronmic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronmic} {phone}\n{address}\n\n'

def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", "a", encoding = "UTF-8") as file:
        file.write(contact_str)
    
def print_contacts():
     with open("phonebook.txt", "r", encoding = "UTF-8") as file:
        contacts_str = file.read()
   
     contacts_list = contacts_str.rstrip().split("\n\n")
     for n, contact in enumerate(contacts_list, 1):
         print(n, contact)
         
def search_contact():
    print(
            "Возможные варианты поиска:\n"
            "1. Фамилия:\n"
            "2. Имя:\n"
            "3. Отчество:\n"
            "4. номер телефона:\n"
            "5. по адресу(городу):\n"
            )
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод!!!")
        var = input("Выберите вариант поиска: ")
    i_var = int(var) - 1

    search = input("Введите данные для поиска: ").title()   
    with open("phonebook.txt", "r", encoding = "UTF-8") as file:
        contacts_str = file.read()
    # print([contacts_str])
    contacts_list = contacts_str.rstrip().split("\n\n")
    # print(contacts_list)
    for str_contact in contacts_list:
        lst_contact = str_contact.replace(":", "").split()
        if search in lst_contact[i_var]:
            print(str_contact) 

def copy_contact():

    with open("phonebook.txt", "r", encoding = "UTF-8") as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split("\n\n")
    for n, contact in enumerate(contacts_list, 1):
         print(n, contact)    

    contact_for_copying = int(input('Введите контакт для копирования: '))   
    print()

    with open("duble_phonebook.txt", "a", encoding = "UTF-8") as file:     
        file.write(f'{contacts_list[contact_for_copying - 1]}\n\n')

def interface():

    with open("phonebook.txt", "a", encoding = "UTF-8"):
        pass
    var = 0    
    while var != "5":
        print(
            "Возможные варианты:\n"
            "1. Добавить контакт:\n"
            "2. Вывести на экран:\n"
            "3. Поиск контакта:\n"
            "4. Копировать контакт:\n"
            "5. Выход "
            )
        print()
        var = input("Выберите вариант действия: ")
        while var not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод!!!")
            var = input("Выберите вариант действия: ")
        print()
        match var:
            case "1":
                add_contact()
            case "2":
                print_contacts()
            case "3":
                search_contact()
            case "4":
                copy_contact()     
            case "5":
                print("До свидания")
        print()

if __name__ == "__main__":  
    interface()
