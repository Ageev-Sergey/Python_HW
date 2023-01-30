
list_lesson = []
studend_book = {}

def Change_rating():
    global studend_book
    name = input('Имя студенда для изменения оценки: ')
    if name in studend_book.keys():
        lesson = input('предмет по которому ученик получил оченку: ')
        for i in studend_book[name]:
            if lesson in i.keys():
                i[lesson] = int(input('input rating: '))
    else:
        print('такого ученика не существует')
        Change_rating()
    print(studend_book)



def Added_new_studend():
    global studend_book
    name = input('Введите имя нового учение: ')
    studend_book[name] = []
    for i in list_lesson:
        print(i)
        print(type(i))
        studend_book[name] += [{i: 0}]
    print(studend_book)



def Added_lesson():
    global studend_book
    lesson = input('Введите название предмета: ')
    for i in studend_book.keys():
        studend_book[i] += [{lesson: 0}]


    list_lesson.append(lesson)
    print(studend_book)


def init_dict():
    list_lesson = []
    global studend_book
    name = input('Введите имя первого учение: ')
    studend_book = {name: []}
    return studend_book
    print(studend_book)
