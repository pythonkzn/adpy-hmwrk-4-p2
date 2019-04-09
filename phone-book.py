import json
import os


class Contact:
    def __init__(self, name, surname, phone_num, fav=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        self.fav = fav
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if str(self.fav) == 'False':
            str_fav = 'Нет'
        else:
            str_fav = 'Да'

        out_str_kwargs = ''
        for key, value in self.kwargs.items():
            out_str_kwargs = out_str_kwargs + '\t' + key + ': ' + value + '\n'

        out_str_args = ''
        for value in self.args:
            out_str_args = '\t' + out_str_args + value

        return ('Имя: ' + self.name + '\n' +
                'Фамилия: ' + self.surname + '\n' +
                'Телефон: ' + self.phone_num + '\n' +
                'В избранных: ' + str_fav + '\n' +
                'Дополнительная информация: ' + '\n' +
                    out_str_kwargs + out_str_args
        )


class PhoneBook:
    def __init__(self, name):
        self.name = name

    def add_contact(self, contact):
        output_data = {'Name': contact.name,
                       'Surname': contact.surname,
                       'Phone_num': contact.phone_num,
                       'Fav': contact.fav,
                       'Add info': contact.args,
                       'Add info 2': contact.kwargs}
        fname = 'contacts.json'
        if os.path.isfile(fname):
            with open(fname,'ab+') as outfile:
                outfile.seek(-1, os.SEEK_END)
                outfile.truncate()
                outfile.write(','.encode())
                outfile.write(json.dumps(output_data).encode())
                outfile.write(']'.encode())
        else:
            with open(fname, 'w') as outfile:
                buf_list = []
                buf_list.append(output_data)
                json.dump(buf_list, outfile)


def in_com_a():  # функция автоматизирующая ввод данных контакта
    in_name = input('Введите имя  ')
    in_surname = input('Введите фамилию  ')
    in_phone_num = input('Введите Номер телефона  ')
    in_fav = input('Введите  1 если избранный контакт, и 2 - если обычный  ')

    key = ''
    ad_dict = {}
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


def in_com_p():
    with open('contacts.json', 'r', encoding='utf8') as file:
        data_print = json.load(file)
        return data_print



def main():
    #john = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    in_com = input('Введите команду: 1) A - для добавления контакта 2) P - для вывода контактов из книги 3) D - для удаления контакта 4) P - для поиска контакта  ')
    if in_com == 'A':
        contact_info = in_com_a()
        new_contact = Contact(contact_info[0], contact_info[1],contact_info[2], contact_info[3], *contact_info[4], **contact_info[5])
        print(new_contact)
        phone_book_1 = PhoneBook('phone_book_1')
        phone_book_1.add_contact(new_contact)
    elif in_com == 'P':
        out_info = in_com_p()
        print(out_info)


if __name__ == "__main__":
        main()






