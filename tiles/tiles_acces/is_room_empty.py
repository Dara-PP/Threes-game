import check_room as check
def is_room_empty(plateau,i,j):
    t=plateau['tiles']
    if check.check_room(plateau,i,j)==True:
        if i == 0 :
            if t[j] == 0:
                return True 
            else :
                return False 
        else: 
            if t[(4*i)+j]==0:
                return True
            else :
                return False 
    else:
        return False 

