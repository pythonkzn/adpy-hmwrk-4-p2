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
            out_str_args = out_str_args + value

        return ('Имя: ' + self.name + '\n' +
                'Фамилия: ' + self.surname + '\n' +
                'Телефон: ' + self.phone_num + '\n' +
                'В избранных: ' + str_fav + '\n' +
                'Дополнительная информация: ' + '\n' +
                    out_str_kwargs + out_str_args)


def main():
    john = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(john)


if __name__ == "__main__":
        main()






