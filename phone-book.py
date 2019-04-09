from modules.contact import Contact
from modules.phone_book import PhoneBook


def in_com_a():  # функция автоматизирующая ввод данных контакта
    in_name = input('Введите имя  ')
    in_surname = input('Введите фамилию  ')
    in_phone_num = input('Введите Номер телефона  ')
    in_fav = input('Введите  1 если избранный контакт, и 2 - если обычный  ')
    key = ''
    in_key_list = []
    in_value_list = []
    while key != 'Q':
        in_key = input('Введите наименование доп. атрибута контакта  ')
        in_value = input('Введите значение доп. атрибута контакта  ')
        in_key_list.append(in_key)
        in_value_list.append(in_value)
        key = input('Введите Q чтобы закончить ввод доп атрибутов и любое значение чтобы продолжить  ')
    ad_dict = dict(zip(in_key_list, in_value_list))
    key = ''
    ad_list = []
    while key != 'Q':
        in_value = input('Введите любую дополнительную информацию ')
        ad_list.append(in_value)
        key = input('Введите Q чтобы закончить ввод дополнительной информации ')
    return [in_name, in_surname, in_phone_num, in_fav, ad_list, ad_dict]


def main():
    phone_book_1 = PhoneBook('phone_book_1')  # создали телефонную книгу
    in_com = input('Введите команду: 1) A - для добавления контакта 2) P - для вывода контактов из книги '
                   '3) D - для удаления контакта 4) PF - для выдачи всех избранных номеров  '
                   '5)FIO - для поиска по имени и фамилии ')
    if in_com == 'A':
        contact_info = in_com_a()
        new_contact = Contact(contact_info[0], contact_info[1],contact_info[2], contact_info[3], *contact_info[4], **contact_info[5])
        phone_book_1.add_contact(new_contact)
        print(new_contact)
    elif in_com == 'P':
        phone_book_1.in_com_p()
    elif in_com == 'D':
        phone_book_1.in_com_d()
    elif in_com == 'PF':
        phone_book_1.in_com_pf()
    elif in_com == 'FIO':
        phone_book_1.in_com_fio()


if __name__ == "__main__":
        main()






