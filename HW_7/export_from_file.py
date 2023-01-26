
def Input_from_file ():

    family_name_new_contact = input('Введите фамилию: ')
    name_new_contact = input('Введите имя: ')
    tel_numbar = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    count = 0

    with open('HW_7/tel_book.txt') as fp:
        for line in fp:
            if line.strip():
                count += 1

    new_contact = str(count + 1) + ' '\
                + family_name_new_contact + ' '\
                + name_new_contact + ' '\
                + tel_numbar + ' '\
                + comment

    with open('HW_7/tel_book.txt', 'a') as data:
        data.writelines(f'{new_contact}\n')
