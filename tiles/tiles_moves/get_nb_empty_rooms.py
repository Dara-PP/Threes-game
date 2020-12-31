def get_nb_empty_rooms(plateau):
    t=plateau['tiles']
    casse_libres=plateau['nombre_case_libres']
    case_count=0
    i=0
    while i < len(t):
        if t[i] == 0:
            case_count+=1
        i+=1
    casse_libres=case_count
    return casse_libres

