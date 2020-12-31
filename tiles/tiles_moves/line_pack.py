def line_pack(plateau,num_lig,debut,sens):
    tab=plateau['tiles']
    lig=num_lig
    col=debut
    if sens == 1 :
        if tab[(4*lig)+col+1]==0:
            x=tab[(4*lig)+col+2]
            tab[(4*lig)+col+1]=x
            tab[(4*lig)+col+2]=0
        else :
            i=0
            while i <= 3 :
                tab[(4*lig)+col] = tab[(4*lig)+col+i]
                if i == 2:
                    tab[(4*lig)+col]=0
                i+=1
                                                                                          
    else :
        if tab[(4*lig)+col-1]==0:
            x=tab[(4*lig)+col-2]
            tab[(4*lig)+col-1]=x
            tab[(4*lig)+col-2]=0
        else:
            i=3
            while i >= 0 :
                tab[(4*lig)+col] = tab[(4*lig)+col-i]
                if i == 0:
                    tab[(4*lig)+col]=0
                i=i-1


    