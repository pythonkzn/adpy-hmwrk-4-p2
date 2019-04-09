import json
import os
from modules.contact import Contact


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

    def in_com_p(self):
        with open('contacts.json', 'r', encoding='utf8') as file:
            data_print = json.load(file)
            for contact in data_print:
                print('***')
                print(Contact(contact['Name'], contact['Surname'], contact['Phone_num'],
                              contact['Fav'], *contact['Add info'], **contact['Add info 2']))

    def in_com_d(self):
        num_del = input('Введите номер телефона контакт которого Вы хотите удалить:  ')
        with open('contacts.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if contact['Phone_num'] == num_del:
                    data.pop(i)
                i += 1
        with open('contacts.json', 'w', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False)
            return data

    def in_com_pf(self):
        with open('contacts.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if contact['Fav'] == '1':
                    print(Contact(contact['Name'], contact['Surname'], contact['Phone_num'],
                              contact['Fav'], *contact['Add info'], **contact['Add info 2']))
                i += 1

    def in_com_fio(self):
        in_name = input('Введите имя ')
        in_surname = input('Введите фамилию ')
        with open('contacts.json', 'r', encoding='utf8') as file:
            data = json.load(file)
            i = 0
            for contact in data:
                if (contact['Name'] == in_name) and (contact['Surname'] == in_surname):
                    print(Contact(contact['Name'], contact['Surname'], contact['Phone_num'],
                              contact['Fav'], *contact['Add info'], **contact['Add info 2']))
                i += 1


