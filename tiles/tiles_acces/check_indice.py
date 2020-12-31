def check_indice(plateau,indice):
    assert isinstance(indice,int),"ERROR"
    n = plateau['n']
    n = n-1
    if indice >= 0:
        if indice <= n:
            return True
        else:
            return False
    else:
        return False
