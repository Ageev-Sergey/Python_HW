import export_from_file as ex
import import_from_file as im
import view

def Start ():
    a = view.batton_click_read_or_writing()
    if a == '1':  # все
        im.Reading_all_file()
    if a == '0':
        flag = view.Batton_click_name_or_id()
        if flag == '1':
            im.Name_po_ID()
        elif flag == '2':
            im.Name_po_alf()
        elif flag == 'q':
            exit
        else:
            Start()
    elif a == "9":
        ex.Input_from_file()
        Start()
    elif a == 'q':
        exit
    else:
        Start()
