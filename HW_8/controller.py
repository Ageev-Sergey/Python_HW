import input_studend
import output
import veiw

def Start ():
    while True:
        flag = veiw.Salect_moves()
        if flag == '1':
            input_studend.init_dict()
        elif flag == '2':
            input_studend.Added_new_studend()
        elif flag == '3':
            input_studend.Added_lesson()
        elif flag == '4':
            input_studend.Change_rating()
        elif flag == '5':
            output.Studend_rating()
        elif flag == '6':
            output.Output_list_studend()
        elif flag == 'q':
            break
        else:
            print('не корректное значение!')
        print()
