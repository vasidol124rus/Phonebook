from data_create import *

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
    # print([contacts_str])
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
    var = input("Выберите вариант плиска: ")
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