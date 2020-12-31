def colum_pack(plateau,num_col,debut,sens):
    tab=plateau['tiles']
    col=num_col
    lig=debut
    if sens == 1 :
        if tab[(4*lig)+col+1]==0:
            x=tab[(4*lig)+col+8]
            tab[(4*lig)+col+4]=x
            tab[(4*lig)+col+8]=0
        else :
            i=0
            while i <= 12 :
                tab[(4*lig)+col] = tab[(4*lig)+col+i]
                if i == 8:
                    tab[(4*lig)+col]=0
                i+=4
                                                                                          
    else :
        if tab[(4*lig)+col-4]==0:
            x=tab[(4*lig)+col-8]
            tab[(4*lig)+col-4]=x
            tab[(4*lig)+col-8]=0
        else:
            i=12
            while i >= 0 :
                tab[(4*lig)+col] = tab[(4*lig)+col-i]
                if i == 0:
                    tab[(4*lig)+col]=0
                i=i-4