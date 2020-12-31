def check_room(plateau,lig,col):
    assert isinstance(lig,int),"ERROR"
    assert isinstance(col,int),"ERROR"
    n=plateau['n']
    n = n - 1
    if lig >= 0 and col >=0 :
        if lig <=n and col <=n: 
            return True
        else :
            return False
    else:
        return False
