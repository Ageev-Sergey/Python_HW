import input_studend


def Studend_rating():
    studend_book = input_studend.studend_book
    print(studend_book)
    name_studend = input('Имя студенда для тображения оценок: ')
    if name_studend in studend_book.keys():
        print(f'оценки {name_studend}:')
        for i in studend_book[name_studend]:
            print(i)
    else:
        print('такого ученика нет')

def Output_list_studend ():
    studend_book = input_studend.studend_book
    for i in studend_book.keys():
        print(i)
