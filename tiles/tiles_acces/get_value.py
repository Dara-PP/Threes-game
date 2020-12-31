import check_room as check
def get_value(plateau,lig,col):
    t = plateau['tiles']
    if check.check_room(plateau,lig,col) == True:
        if lig == 0:
            return t[col]
        else:
            return t[(4*lig)+col]
    else:
        return False
