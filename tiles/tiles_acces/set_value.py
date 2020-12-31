def set_value(plateau,lig,col,val):
	assert (val >= 0),"ERROR"
    t = plateau['tiles']
    if check_room(plateau,lig,col) == True:
        if lig == 0:
            t[col] = val
            plateau['nombre_case_libres'] = plateau['nombre_case_libres'] - 1
        else:
            t[(4*lig)+col] = val
            plateau['nombre_case_libres'] = plateau['nombre_case_libres'] - 1
    else:
        return False
    
