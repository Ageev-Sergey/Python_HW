def Name_po_ID ():
    with open('HW_7/tel_book.txt', 'r') as data:
            list_FO_str = [i for i in data]
    print(f'\n   по ID:')
    for i in list_FO_str:
        i = i.split(' ')
        print(i[1] + ' ' + i[2])


def Name_po_alf ():
    with open('HW_7/tel_book.txt', 'r') as data:
            list_FO_str = [i for i in data]

    list_FO = []
    for i in list_FO_str:
        i = i.split(' ')
        list_FO += [i[1] + ' ' + i[2]]

    print(f'\n   по Алфавиту:')

    list_FO = sorted(list_FO)
    for i in list_FO:
        print(i)


def Reading_all_file():
    with open('HW_7/tel_book.txt', 'r') as data:
        tel_book = data.read()
    print(tel_book)
